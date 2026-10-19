#!/usr/bin/env python3
"""
Project Sorcery - AI Bot Deep Q-Network (DQN) & 1v1 Simulation Suite
===================================================================
Conducts 1v1 matches across the 100-bot population using Deep Q-Networks (DQN / Double DQN)
with Action Masking, Experience Replay, and Sequential Phase Curriculum Training.

Key Features:
- Action-Masked Double DQN: Strictly restricts action selection & Bellman targets
  to valid, craftable spells based on the wizard's live rune pool.
- 80-feature observation vector processing (75 tactical + 5 normalized rune counts).
- Experience Replay Buffer with dual-perspective transition collection (both Player 1
  and Player 2 transitions captured per turn).
- Shaped Rewards: Turn damage differential, combo setup progress, and terminal match outcome.
- Sequential Phase Curriculum Training: Traverses Stages 1 -> 2 -> 3 -> 4 -> Standard Duels
  from training_stages.json to solve the RL exploration bottleneck on complex combos.
- Full Backward Compatibility with balance_tuner.py and existing game engine APIs.
"""

import argparse
import copy
import json
import math
import os
import random
import sys
import time
from collections import deque
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

import numpy as np

# Ensure project_sorcery engine can be imported
SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

# Search fallback locations for project_sorcery
for search_dir in [
    SCRIPT_DIR,
    SCRIPT_DIR.parent,
    SCRIPT_DIR / "downloads",
    SCRIPT_DIR.parent / "downloads",
    SCRIPT_DIR / "project_sorcery_simulation",
]:
    if search_dir.exists() and str(search_dir) not in sys.path:
        sys.path.append(str(search_dir))

try:
    from project_sorcery import (
        ProjectSorceryGame,
        Wizard,
        get_registry,
        get_spell_class,
        PREFIX_TO_CLASS,
        MULTI_CONDITION_REQUIREMENTS,
        get_castable_spells_from_pool,
        evaluate_multi_condition_score,
    )
except ImportError:
    try:
        from project_sorcery_simulation.project_sorcery import (
            ProjectSorceryGame,
            Wizard,
            get_registry,
            get_spell_class,
            PREFIX_TO_CLASS,
            MULTI_CONDITION_REQUIREMENTS,
            get_castable_spells_from_pool,
            evaluate_multi_condition_score,
        )
    except ImportError as e:
        raise ImportError(f"Could not import project_sorcery engine: {e}")


def resolve_file_path(filename: str, custom_path: Optional[str] = None) -> Path:
    """Finds a file in common project directories."""
    if custom_path and os.path.exists(custom_path):
        return Path(custom_path).resolve()

    candidate_dirs = [
        SCRIPT_DIR,
        SCRIPT_DIR / "project_sorcery_simulation",
        SCRIPT_DIR.parent / "project_sorcery_simulation",
        Path.cwd() / "project_sorcery_simulation",
        Path.cwd(),
        SCRIPT_DIR / "downloads",
        SCRIPT_DIR.parent / "downloads",
        Path.cwd() / "downloads",
    ]

    for d in candidate_dirs:
        p = d / filename
        if p.exists():
            return p.resolve()

    return (SCRIPT_DIR / filename).resolve()


def migrate_dna_registry(data: Dict[str, Any]) -> int:
    """
    Pads existing 75-feature weights_layer_1 arrays with 5 rows of small random weights
    to adapt to the 80-feature observation vector, preventing matrix multiplication crashes.
    """
    migrated = 0
    for bot in data.get("bots", []):
        dna = bot.get("dna", {})
        if "weights_layer_1" not in dna:
            continue
        w1 = np.array(dna["weights_layer_1"], dtype=np.float32)
        if w1.shape[0] < 80 and w1.shape[0] > 0:
            needed = 80 - w1.shape[0]
            pad = np.random.normal(0.0, 0.05, size=(needed, w1.shape[1])).astype(np.float32)
            new_w1 = np.vstack([w1, pad])
            dna["weights_layer_1"] = [[round(float(v), 4) for v in row] for row in np.round(new_w1, 4).tolist()]
            dna["architecture"] = [80, 48, 32, 125]
            dna["total_parameters"] = 80 * 48 + 48 + 48 * 32 + 32 + 32 * 125 + 125
            migrated += 1

    meta = data.setdefault("meta", {})
    model_arch = meta.setdefault("model_architecture", {})
    model_arch["input_dimension"] = 80
    model_arch["total_parameters_per_bot"] = 9581
    model_arch["input_feature_description"] = (
        "80 normalized features (75 tactical + 5 normalized rune counts F,W,E,L,D) "
        "extracted via ProjectSorceryGame.get_observation_vector(player_idx)"
    )
    return migrated


# =============================================================================
# 1. DEEP Q-NETWORK (DQN) ARCHITECTURE & VECTORIZED NUMPY OPTIMIZER
# =============================================================================

class QNetwork:
    """
    Feedforward Multi-Layer Perceptron (MLP) Q-Network for Project Sorcery.
    Architecture: [80 inputs -> 48 LeakyReLU -> 32 LeakyReLU -> 125 Q-values]
    """

    def __init__(
        self,
        input_dim: int = 80,
        hidden1: int = 48,
        hidden2: int = 32,
        output_dim: int = 125,
        alpha: float = 0.01,
        weights_dict: Optional[Dict[str, Any]] = None,
    ):
        self.input_dim = input_dim
        self.hidden1 = hidden1
        self.hidden2 = hidden2
        self.output_dim = output_dim
        self.alpha = alpha  # LeakyReLU slope

        if weights_dict and "weights_layer_1" in weights_dict:
            self.load_from_dict(weights_dict)
        else:
            self.reset_parameters()

    def reset_parameters(self) -> None:
        """Kaiming / He normal initialization for LeakyReLU networks."""
        self.w1 = (np.random.randn(self.input_dim, self.hidden1).astype(np.float32)
                   * np.sqrt(2.0 / self.input_dim))
        self.b1 = np.zeros(self.hidden1, dtype=np.float32)

        self.w2 = (np.random.randn(self.hidden1, self.hidden2).astype(np.float32)
                   * np.sqrt(2.0 / self.hidden1))
        self.b2 = np.zeros(self.hidden2, dtype=np.float32)

        self.w3 = (np.random.randn(self.hidden2, self.output_dim).astype(np.float32)
                   * np.sqrt(2.0 / self.hidden2))
        self.b3 = np.zeros(self.output_dim, dtype=np.float32)

    def load_from_dict(self, d: Dict[str, Any]) -> None:
        """Loads weights and biases from bot DNA or checkpoint dictionary."""
        w1_arr = np.array(d["weights_layer_1"], dtype=np.float32)
        if w1_arr.shape[0] < self.input_dim:
            pad = np.random.normal(0.0, 0.05, size=(self.input_dim - w1_arr.shape[0], w1_arr.shape[1])).astype(np.float32)
            w1_arr = np.vstack([w1_arr, pad])
        self.w1 = w1_arr[:self.input_dim, :self.hidden1]
        self.b1 = np.array(d["biases_layer_1"], dtype=np.float32)[:self.hidden1]

        self.w2 = np.array(d["weights_layer_2"], dtype=np.float32)[:self.hidden1, :self.hidden2]
        self.b2 = np.array(d["biases_layer_2"], dtype=np.float32)[:self.hidden2]

        self.w3 = np.array(d["weights_layer_3"], dtype=np.float32)[:self.hidden2, :self.output_dim]
        self.b3 = np.array(d["biases_layer_3"], dtype=np.float32)[:self.output_dim]

    def to_dict(self) -> Dict[str, Any]:
        """Serializes weights and biases into DNA dictionary format."""
        return {
            "architecture": [self.input_dim, self.hidden1, self.hidden2, self.output_dim],
            "total_parameters": (self.input_dim * self.hidden1 + self.hidden1 +
                                 self.hidden1 * self.hidden2 + self.hidden2 +
                                 self.hidden2 * self.output_dim + self.output_dim),
            "weights_layer_1": [[round(float(v), 4) for v in row] for row in self.w1.tolist()],
            "biases_layer_1": [round(float(v), 4) for v in self.b1.tolist()],
            "weights_layer_2": [[round(float(v), 4) for v in row] for row in self.w2.tolist()],
            "biases_layer_2": [round(float(v), 4) for v in self.b2.tolist()],
            "weights_layer_3": [[round(float(v), 4) for v in row] for row in self.w3.tolist()],
            "biases_layer_3": [round(float(v), 4) for v in self.b3.tolist()],
        }

    def forward(self, x: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """
        Forward pass.
        Returns:
            z1, h1, z2, h2, q
        """
        # Ensure 2D (batch_size, input_dim)
        if x.ndim == 1:
            x_in = x[np.newaxis, :self.input_dim]
        else:
            x_in = x[:, :self.input_dim]

        z1 = np.dot(x_in, self.w1) + self.b1
        h1 = np.where(z1 > 0, z1, z1 * self.alpha)

        z2 = np.dot(h1, self.w2) + self.b2
        h2 = np.where(z2 > 0, z2, z2 * self.alpha)

        q = np.dot(h2, self.w3) + self.b3
        return z1, h1, z2, h2, q

    def compute_q(self, x: np.ndarray) -> np.ndarray:
        """Convenience method returning only output Q-values."""
        _, _, _, _, q = self.forward(x)
        return q

    def copy_weights_from(self, source: "QNetwork", tau: float = 1.0) -> None:
        """Copies or soft-updates weights from source network."""
        if tau >= 1.0:
            self.w1 = np.copy(source.w1)
            self.b1 = np.copy(source.b1)
            self.w2 = np.copy(source.w2)
            self.b2 = np.copy(source.b2)
            self.w3 = np.copy(source.w3)
            self.b3 = np.copy(source.b3)
        else:
            self.w1 = (1.0 - tau) * self.w1 + tau * source.w1
            self.b1 = (1.0 - tau) * self.b1 + tau * source.b1
            self.w2 = (1.0 - tau) * self.w2 + tau * source.w2
            self.b2 = (1.0 - tau) * self.b2 + tau * source.b2
            self.w3 = (1.0 - tau) * self.w3 + tau * source.w3
            self.b3 = (1.0 - tau) * self.b3 + tau * source.b3


class AdamOptimizer:
    """Vectorized Adam optimizer for training NumPy QNetworks."""

    def __init__(
        self,
        network: QNetwork,
        lr: float = 0.001,
        beta1: float = 0.9,
        beta2: float = 0.999,
        eps: float = 1e-8,
        weight_decay: float = 1e-4,
    ):
        self.network = network
        self.lr = lr
        self.beta1 = beta1
        self.beta2 = beta2
        self.eps = eps
        self.weight_decay = weight_decay
        self.t = 0

        # Initialize moments for each parameter
        self.m_w1 = np.zeros_like(network.w1)
        self.v_w1 = np.zeros_like(network.w1)
        self.m_b1 = np.zeros_like(network.b1)
        self.v_b1 = np.zeros_like(network.b1)

        self.m_w2 = np.zeros_like(network.w2)
        self.v_w2 = np.zeros_like(network.w2)
        self.m_b2 = np.zeros_like(network.b2)
        self.v_b2 = np.zeros_like(network.b2)

        self.m_w3 = np.zeros_like(network.w3)
        self.v_w3 = np.zeros_like(network.w3)
        self.m_b3 = np.zeros_like(network.b3)
        self.v_b3 = np.zeros_like(network.b3)

    def _update_param(
        self, param: np.ndarray, grad: np.ndarray, m: np.ndarray, v: np.ndarray
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        # Optional weight decay (L2 regularization)
        if self.weight_decay > 0.0:
            grad = grad + self.weight_decay * param

        m = self.beta1 * m + (1.0 - self.beta1) * grad
        v = self.beta2 * v + (1.0 - self.beta2) * (grad ** 2)

        m_hat = m / (1.0 - (self.beta1 ** self.t))
        v_hat = v / (1.0 - (self.beta2 ** self.t))

        updated_param = param - self.lr * m_hat / (np.sqrt(v_hat) + self.eps)
        return updated_param, m, v

    def step(
        self,
        gw1: np.ndarray,
        gb1: np.ndarray,
        gw2: np.ndarray,
        gb2: np.ndarray,
        gw3: np.ndarray,
        gb3: np.ndarray,
        max_grad_norm: float = 5.0,
    ) -> None:
        self.t += 1

        # Global gradient clipping
        total_norm_sq = (
            np.sum(gw1 ** 2) + np.sum(gb1 ** 2) +
            np.sum(gw2 ** 2) + np.sum(gb2 ** 2) +
            np.sum(gw3 ** 2) + np.sum(gb3 ** 2)
        )
        total_norm = np.sqrt(total_norm_sq)
        if total_norm > max_grad_norm and total_norm > 0:
            scale = max_grad_norm / total_norm
            gw1 *= scale
            gb1 *= scale
            gw2 *= scale
            gb2 *= scale
            gw3 *= scale
            gb3 *= scale

        self.network.w1, self.m_w1, self.v_w1 = self._update_param(self.network.w1, gw1, self.m_w1, self.v_w1)
        self.network.b1, self.m_b1, self.v_b1 = self._update_param(self.network.b1, gb1, self.m_b1, self.v_b1)

        self.network.w2, self.m_w2, self.v_w2 = self._update_param(self.network.w2, gw2, self.m_w2, self.v_w2)
        self.network.b2, self.m_b2, self.v_b2 = self._update_param(self.network.b2, gb2, self.m_b2, self.v_b2)

        self.network.w3, self.m_w3, self.v_w3 = self._update_param(self.network.w3, gw3, self.m_w3, self.v_w3)
        self.network.b3, self.m_b3, self.v_b3 = self._update_param(self.network.b3, gb3, self.m_b3, self.v_b3)


class ReplayBuffer:
    """Experience replay buffer for storing multi-turn 1v1 transitions."""

    def __init__(self, capacity: int = 50000, state_dim: int = 80, action_dim: int = 125):
        self.capacity = capacity
        self.state_dim = state_dim
        self.action_dim = action_dim

        self.states = np.zeros((capacity, state_dim), dtype=np.float32)
        self.actions = np.zeros(capacity, dtype=np.int64)
        self.rewards = np.zeros(capacity, dtype=np.float32)
        self.next_states = np.zeros((capacity, state_dim), dtype=np.float32)
        self.next_masks = np.zeros((capacity, action_dim), dtype=np.float32)
        self.dones = np.zeros(capacity, dtype=np.float32)

        self.ptr = 0
        self.size = 0

    def push(
        self,
        state: np.ndarray,
        action_idx: int,
        reward: float,
        next_state: np.ndarray,
        next_mask: np.ndarray,
        done: bool,
    ) -> None:
        idx = self.ptr
        self.states[idx] = state[:self.state_dim]
        self.actions[idx] = action_idx
        self.rewards[idx] = reward
        self.next_states[idx] = next_state[:self.state_dim]
        self.next_masks[idx] = next_mask[:self.action_dim]
        self.dones[idx] = 1.0 if done else 0.0

        self.ptr = (self.ptr + 1) % self.capacity
        self.size = min(self.size + 1, self.capacity)

    def sample(self, batch_size: int) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        idxs = np.random.randint(0, self.size, size=batch_size)
        return (
            self.states[idxs],
            self.actions[idxs],
            self.rewards[idxs],
            self.next_states[idxs],
            self.next_masks[idxs],
            self.dones[idxs],
        )

    def __len__(self) -> int:
        return self.size


class DQNAgent:
    """
    Deep Q-Network Agent with Action Masking, Double DQN loss,
    and adaptive epsilon exploration.
    """

    def __init__(
        self,
        action_catalog: List[str],
        lr: float = 0.001,
        gamma: float = 0.98,
        epsilon: float = 0.8,
        epsilon_min: float = 0.05,
        epsilon_decay: float = 0.998,
        tau: float = 0.005,
        buffer_capacity: int = 50000,
        batch_size: int = 64,
        weights_dict: Optional[Dict[str, Any]] = None,
        eval_epsilon: float = 0.08,
    ):
        self.action_catalog = action_catalog
        self.action_to_idx = {r: i for i, r in enumerate(action_catalog)}
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_decay = epsilon_decay
        self.tau = tau
        self.batch_size = batch_size
        self.eval_epsilon = eval_epsilon

        self.online_net = QNetwork(weights_dict=weights_dict)
        self.target_net = QNetwork()
        self.target_net.copy_weights_from(self.online_net, tau=1.0)

        self.optimizer = AdamOptimizer(self.online_net, lr=lr)
        self.replay_buffer = ReplayBuffer(capacity=buffer_capacity)

        self.train_steps = 0
        self.losses: List[float] = []

    def get_action_mask(self, obs: Dict[str, Any]) -> np.ndarray:
        """Returns 125-dim binary mask where 1.0 = valid/castable spell, 0.0 = invalid."""
        me_info = obs.get("me", {})
        rune_pool = me_info.get("rune_pool", [])
        castable = me_info.get("castable_spells", obs.get("castable_spells", []))
        if not castable and rune_pool:
            castable = get_castable_spells_from_pool(rune_pool, self.action_catalog)

        mask = np.zeros(len(self.action_catalog), dtype=np.float32)
        for spell in castable:
            idx = self.action_to_idx.get(spell)
            if idx is not None:
                mask[idx] = 1.0

        # Safety fallback: if no spells castable, allow all
        if np.sum(mask) == 0:
            mask[:] = 1.0
        return mask

    def select_action(
        self,
        obs: Dict[str, Any],
        eval_mode: bool = False,
        forced_exploration_rate: Optional[float] = None,
    ) -> str:
        """
        Action-Masked Epsilon-Greedy action selection.
        Sets uncraftable spell logits to -1e9.
        If forced_exploration_rate is provided, uses that exploration probability.
        In eval_mode, defaults to forced_exploration_rate or self.eval_epsilon (0.08).
        """
        mask = self.get_action_mask(obs)
        valid_indices = np.where(mask > 0.5)[0]

        # Determine effective exploration probability
        if forced_exploration_rate is not None:
            explore_prob = forced_exploration_rate
        elif eval_mode:
            explore_prob = getattr(self, "eval_epsilon", 0.08)
        else:
            explore_prob = self.epsilon

        # Epsilon-random exploration over VALID spells
        if explore_prob > 0.0 and random.random() < explore_prob and len(valid_indices) > 0:
            chosen_idx = int(np.random.choice(valid_indices))
            return self.action_catalog[chosen_idx]

        # Q-Network Forward Pass (pure learned Q-values without hardcoded spell biases)
        feat_vec = np.array(obs.get("feature_vector", []), dtype=np.float32)
        q_values = self.online_net.compute_q(feat_vec)[0]

        # ACTION MASKING: Set uncraftable spells to -1e9
        q_masked = np.where(mask > 0.5, q_values, -1e9)
        if eval_mode and len(valid_indices) > 1:
            # Boltzmann (softmax) action selection over valid castable spells in eval mode
            # so pick rates respond smoothly to Q-value shifts without deterministic argmax lock-in
            eval_temp = float(getattr(self, "eval_temperature", 0.25))
            valid_q = q_values[valid_indices] / max(1e-4, eval_temp)
            valid_q = valid_q - np.max(valid_q)
            exp_q = np.exp(np.clip(valid_q, -20.0, 0.0))
            probs = exp_q / np.sum(exp_q)
            chosen_idx = int(np.random.choice(valid_indices, p=probs))
            return self.action_catalog[chosen_idx]

        chosen_idx = int(np.argmax(q_masked))
        return self.action_catalog[chosen_idx]

    def train_step(self) -> float:
        """Performs one Double-DQN gradient step with action masking."""
        if len(self.replay_buffer) < self.batch_size:
            return 0.0

        states, actions, rewards, next_states, next_masks, dones = self.replay_buffer.sample(self.batch_size)

        # 1. Double DQN target computation:
        # a* = argmax_{a' in valid} Q_online(s', a')
        next_q_online = self.online_net.compute_q(next_states)
        next_q_online_masked = np.where(next_masks > 0.5, next_q_online, -1e9)
        best_next_actions = np.argmax(next_q_online_masked, axis=1)

        # Q_target(s', a*)
        next_q_target = self.target_net.compute_q(next_states)
        q_target_values = next_q_target[np.arange(self.batch_size), best_next_actions]

        # Bellman Target: y = r + (1 - done) * gamma * Q_target(s', a*)
        targets = rewards + (1.0 - dones) * self.gamma * q_target_values

        # 2. Forward pass on online network
        z1, h1, z2, h2, q_pred = self.online_net.forward(states)
        q_pred_selected = q_pred[np.arange(self.batch_size), actions]

        # 3. Huber / Smooth L1 Loss & Gradient
        diff = q_pred_selected - targets
        diff_abs = np.abs(diff)
        loss = float(np.where(diff_abs <= 1.0, 0.5 * (diff ** 2), diff_abs - 0.5).mean())
        grad_selected = np.where(diff_abs <= 1.0, diff, np.sign(diff)) / self.batch_size

        # 4. Backward Pass through MLP layers
        grad_q = np.zeros_like(q_pred)
        grad_q[np.arange(self.batch_size), actions] = grad_selected

        gw3 = np.dot(h2.T, grad_q)
        gb3 = np.sum(grad_q, axis=0)

        grad_h2 = np.dot(grad_q, self.online_net.w3.T)
        grad_z2 = grad_h2 * np.where(z2 > 0, 1.0, self.online_net.alpha)

        gw2 = np.dot(h1.T, grad_z2)
        gb2 = np.sum(grad_z2, axis=0)

        grad_h1 = np.dot(grad_z2, self.online_net.w2.T)
        grad_z1 = grad_h1 * np.where(z1 > 0, 1.0, self.online_net.alpha)

        gw1 = np.dot(states.T, grad_z1)
        gb1 = np.sum(grad_z1, axis=0)

        # 5. Optimizer Step
        self.optimizer.step(gw1, gb1, gw2, gb2, gw3, gb3)

        # 6. Soft update target network: theta_target = (1 - tau)*theta_target + tau*theta_online
        self.target_net.copy_weights_from(self.online_net, tau=self.tau)

        # 7. Decay exploration rate
        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)
        self.train_steps += 1
        self.losses.append(loss)
        return loss


# =============================================================================
# 2. BOT POLICY ADAPTER (COMPATIBILITY WRAPPER)
# =============================================================================

class NeuralBotPolicy:
    """
    Policy adapter for Project Sorcery AI Bots.
    Wraps bot DNA weights or a DQNAgent to evaluate action choices.
    """

    def __init__(
        self,
        bot_dict: Dict[str, Any],
        action_catalog: List[str],
        dqn_agent: Optional[DQNAgent] = None,
        eval_mode: bool = False,
        forced_exploration_rate: Optional[float] = None,
    ):
        self.bot_id = bot_dict.get("bot_id", "Unknown")
        self.name = self.bot_id
        self.action_catalog = action_catalog
        self.dqn_agent = dqn_agent
        self.eval_mode = eval_mode
        self.forced_exploration_rate = forced_exploration_rate
        self.memory: List[Dict[str, Any]] = []

        dna = bot_dict.get("dna", {})
        self.bot_network = QNetwork(weights_dict=dna) if dna else None
        hyperparams = bot_dict.get("genetic_hyperparameters", {})
        self.temperature = float(hyperparams.get("temperature", 0.35))
        self.decision_mode = hyperparams.get("decision_mode", "softmax_sample")

        if dqn_agent is None:
            self.network = self.bot_network if self.bot_network is not None else QNetwork()
        else:
            self.network = dqn_agent.online_net

    def __call__(self, obs: Dict[str, Any]) -> str:
        """Takes game state dict and outputs a valid, craftable 3-rune recipe."""
        feature_vec = obs.get("feature_vector")
        if feature_vec is None:
            raise ValueError(f"Observation missing 'feature_vector' for bot {self.bot_id}")

        me_info = obs.get("me", {})
        rune_pool = me_info.get("rune_pool", [])
        castable_spells = me_info.get("castable_spells", obs.get("castable_spells", []))
        if not castable_spells and rune_pool:
            castable_spells = get_castable_spells_from_pool(rune_pool, self.action_catalog)

        # Determine effective exploration probability
        if self.forced_exploration_rate is not None:
            explore_prob = self.forced_exploration_rate
        elif self.eval_mode:
            explore_prob = getattr(self.dqn_agent, "eval_epsilon", 0.08) if self.dqn_agent else 0.08
        elif self.dqn_agent is not None:
            explore_prob = self.dqn_agent.epsilon
        else:
            explore_prob = 0.0

        if explore_prob > 0.0 and random.random() < explore_prob and castable_spells:
            return random.choice(castable_spells)

        feat_arr = np.array(feature_vec, dtype=np.float32)
        if self.dqn_agent is not None and self.bot_network is not None:
            # Blend shared online Q-network with individual bot DNA network for symmetric, diverse evaluation
            q_online = self.dqn_agent.online_net.compute_q(feat_arr)[0]
            q_bot = self.bot_network.compute_q(feat_arr)[0]
            q_values = 0.75 * q_online + 0.25 * q_bot
        elif self.dqn_agent is not None:
            q_values = self.dqn_agent.online_net.compute_q(feat_arr)[0]
        else:
            q_values = self.network.compute_q(feat_arr)[0]

        if castable_spells:
            castable_set = set(castable_spells)
            for idx, recipe in enumerate(self.action_catalog):
                if recipe not in castable_set:
                    q_values[idx] = -1e9

        valid_mask = q_values > -1e8
        if not np.any(valid_mask):
            return random.choice(self.action_catalog)

        # In training mode with dqn_agent, use greedy argmax after epsilon check;
        # in eval_mode or standalone softmax_sample mode, use temperature-scaled Boltzmann sampling
        if not self.eval_mode and self.dqn_agent is not None:
            action_idx = int(np.argmax(q_values))
        elif self.eval_mode or self.decision_mode == "softmax_sample":
            eff_temp = max(0.15, min(0.50, self.temperature * 0.35)) if self.eval_mode else max(1e-5, self.temperature)
            scaled = q_values / eff_temp
            shifted = np.where(valid_mask, scaled - np.max(scaled[valid_mask]), -np.inf)
            exp_q = np.where(valid_mask, np.exp(np.clip(shifted, -20.0, 0.0)), 0.0)
            sum_exp = np.sum(exp_q)
            probs = exp_q / sum_exp if sum_exp > 0 else np.where(valid_mask, 1.0, 0.0) / np.sum(valid_mask)
            action_idx = int(np.random.choice(len(probs), p=probs))
        else:
            action_idx = int(np.argmax(q_values))

        return self.action_catalog[action_idx]


def create_wizard_for_bot(bot: Dict[str, Any]) -> Wizard:
    """Creates a Wizard entity for a bot with standard base stats."""
    w_stats = bot.get("wizard_stats", {})
    bot_id = bot.get("bot_id", "Wizard")
    wiz = Wizard(
        name=bot_id,
        starting_hp=float(w_stats.get("starting_hp", 1000.0)),
        base_potency=float(w_stats.get("base_potency", 100.0)),
        base_defense=float(w_stats.get("base_defense", 100.0)),
        base_luck=float(w_stats.get("base_luck", 100.0)),
        base_speed=float(w_stats.get("base_speed", 100.0)),
    )
    wiz.bot_id = bot_id
    return wiz


def count_active_combo_conditions(caster: Wizard, target: Wizard, env: Any) -> int:
    """Counts active conditions (weather, location, buffs, debuffs) for combo scoring."""
    count = 0
    if getattr(env, "weather", None) and env.weather.value != "Clear":
        count += 1
    if getattr(env, "location", None):
        count += 1
    count += len(getattr(caster, "buffs", {}))
    count += len(getattr(target, "debuffs", {}))
    return count


# =============================================================================
# 3. 1v1 DUEL EXECUTION & REWARD SHAPING
# =============================================================================

def play_duel(
    bot_a: Dict[str, Any],
    bot_b: Dict[str, Any],
    action_catalog: List[str],
    spell_data_path: str,
    max_turns: int = 50,
    initial_board_state: Optional[Dict[str, Any]] = None,
    dqn_agent: Optional[DQNAgent] = None,
    record_experience: bool = True,
    eval_mode: bool = False,
    forced_exploration_rate: Optional[float] = None,
) -> Dict[str, Any]:
    """
    Conducts a single 1v1 duel between bot_a and bot_b.
    Collects step transitions into dqn_agent.replay_buffer when record_experience is True.
    Calculates shaped rewards (turn damage differential + combo progress + terminal outcome).
    """
    wiz_a = create_wizard_for_bot(bot_a)
    wiz_b = create_wizard_for_bot(bot_b)

    policy_a = NeuralBotPolicy(
        bot_a,
        action_catalog,
        dqn_agent=dqn_agent,
        eval_mode=eval_mode,
        forced_exploration_rate=forced_exploration_rate,
    )
    policy_b = NeuralBotPolicy(
        bot_b,
        action_catalog,
        dqn_agent=dqn_agent,
        eval_mode=eval_mode,
        forced_exploration_rate=forced_exploration_rate,
    )

    game = ProjectSorceryGame(
        player1=wiz_a,
        player2=wiz_b,
        spell_data_path=spell_data_path,
        max_turns=max_turns,
    )

    obs_a, obs_b = game.reset(initial_board_state=initial_board_state)

    peak_conditions_a = count_active_combo_conditions(wiz_a, wiz_b, game.env)
    peak_conditions_b = count_active_combo_conditions(wiz_b, wiz_a, game.env)

    prev_dmg_dealt_a = 0.0
    prev_dmg_taken_a = 0.0
    prev_heal_done_a = 0.0
    prev_dmg_dealt_b = 0.0
    prev_dmg_taken_b = 0.0
    prev_heal_done_b = 0.0

    action_to_idx = {r: i for i, r in enumerate(action_catalog)}

    # Track episode transitions for both perspectives
    transitions_a = []
    transitions_b = []

    while not game.is_over:
        state_vec_a = np.array(obs_a.get("feature_vector", []), dtype=np.float32)
        state_vec_b = np.array(obs_b.get("feature_vector", []), dtype=np.float32)

        action_a = policy_a(obs_a)
        action_b = policy_b(obs_b)

        idx_a = action_to_idx.get(action_a, 0)
        idx_b = action_to_idx.get(action_b, 0)

        obs_a_next, obs_b_next, r1, r2, done, info = game.step(action_a, action_b)

        # Track peak conditions
        curr_cond_a = count_active_combo_conditions(wiz_a, wiz_b, game.env)
        curr_cond_b = count_active_combo_conditions(wiz_b, wiz_a, game.env)
        cond_adv_a = max(0, curr_cond_a - peak_conditions_a)
        cond_adv_b = max(0, curr_cond_b - peak_conditions_b)
        peak_conditions_a = max(peak_conditions_a, curr_cond_a)
        peak_conditions_b = max(peak_conditions_b, curr_cond_b)

        # Turn damage & healing differential
        turn_dmg_dealt_a = wiz_a.damage_dealt - prev_dmg_dealt_a
        turn_dmg_taken_a = wiz_a.damage_taken - prev_dmg_taken_a
        turn_heal_a = wiz_a.healing_done - prev_heal_done_a
        prev_dmg_dealt_a = wiz_a.damage_dealt
        prev_dmg_taken_a = wiz_a.damage_taken
        prev_heal_done_a = wiz_a.healing_done

        turn_dmg_dealt_b = wiz_b.damage_dealt - prev_dmg_dealt_b
        turn_dmg_taken_b = wiz_b.damage_taken - prev_dmg_taken_b
        turn_heal_b = wiz_b.healing_done - prev_heal_done_b
        prev_dmg_dealt_b = wiz_b.damage_dealt
        prev_dmg_taken_b = wiz_b.damage_taken
        prev_heal_done_b = wiz_b.healing_done

        # Shaped turn rewards (net health swing including healing + modest combo setup progress)
        net_swing_a = (turn_dmg_dealt_a + turn_heal_a) - (turn_dmg_taken_a + turn_heal_b)
        net_swing_b = (turn_dmg_dealt_b + turn_heal_b) - (turn_dmg_taken_b + turn_heal_a)
        r_step_a = net_swing_a / 1000.0 + 0.015 * cond_adv_a
        r_step_b = net_swing_b / 1000.0 + 0.015 * cond_adv_b

        next_state_vec_a = np.array(obs_a_next.get("feature_vector", []), dtype=np.float32)
        next_state_vec_b = np.array(obs_b_next.get("feature_vector", []), dtype=np.float32)

        mask_a_next = dqn_agent.get_action_mask(obs_a_next) if dqn_agent else np.ones(len(action_catalog), dtype=np.float32)
        mask_b_next = dqn_agent.get_action_mask(obs_b_next) if dqn_agent else np.ones(len(action_catalog), dtype=np.float32)

        transitions_a.append((state_vec_a, idx_a, r_step_a, next_state_vec_a, mask_a_next, done))
        transitions_b.append((state_vec_b, idx_b, r_step_b, next_state_vec_b, mask_b_next, done))

        obs_a = obs_a_next
        obs_b = obs_b_next

    # Determine Winner
    if game.winner == wiz_a.name:
        winner_bot = bot_a
        loser_bot = bot_b
        winner_wiz = wiz_a
        loser_wiz = wiz_b
        result_type = "win_p1"
        s_outcome_a = 1.0
        s_outcome_b = -1.0
    elif game.winner == wiz_b.name:
        winner_bot = bot_b
        loser_bot = bot_a
        winner_wiz = wiz_b
        loser_wiz = wiz_a
        result_type = "win_p2"
        s_outcome_a = -1.0
        s_outcome_b = 1.0
    else:
        if wiz_a.current_health > wiz_b.current_health:
            winner_bot, loser_bot = bot_a, bot_b
            winner_wiz, loser_wiz = wiz_a, wiz_b
            result_type = "tiebreaker_p1"
            s_outcome_a = 1.0
            s_outcome_b = -1.0
        elif wiz_b.current_health > wiz_a.current_health:
            winner_bot, loser_bot = bot_b, bot_a
            winner_wiz, loser_wiz = wiz_b, wiz_a
            result_type = "tiebreaker_p2"
            s_outcome_a = -1.0
            s_outcome_b = 1.0
        else:
            if random.random() < 0.5:
                winner_bot, loser_bot = bot_a, bot_b
                winner_wiz, loser_wiz = wiz_a, wiz_b
                s_outcome_a = 1.0
                s_outcome_b = -1.0
            else:
                winner_bot, loser_bot = bot_b, bot_a
                winner_wiz, loser_wiz = wiz_b, wiz_a
                s_outcome_a = -1.0
                s_outcome_b = 1.0
            result_type = "tiebreaker_draw_resolved"

    # Terminal outcome reward addition to final transition
    terminal_bonus_a = 1.0 if winner_bot is bot_a else (-1.0 if winner_bot is bot_b else 0.0)
    terminal_bonus_b = 1.0 if winner_bot is bot_b else (-1.0 if winner_bot is bot_a else 0.0)

    if record_experience and dqn_agent is not None and not eval_mode:
        for i, (s, a, r, s_n, m_n, d) in enumerate(transitions_a):
            r_tot = r + (terminal_bonus_a if i == len(transitions_a) - 1 else 0.0)
            dqn_agent.replay_buffer.push(s, a, r_tot, s_n, m_n, d)

        for i, (s, a, r, s_n, m_n, d) in enumerate(transitions_b):
            r_tot = r + (terminal_bonus_b if i == len(transitions_b) - 1 else 0.0)
            dqn_agent.replay_buffer.push(s, a, r_tot, s_n, m_n, d)

    # Telemetry and spell usage extraction
    spells_cast_a: Dict[str, int] = {}
    spells_cast_b: Dict[str, int] = {}
    classes_used_a: Dict[str, int] = {}
    classes_used_b: Dict[str, int] = {}

    for turn_entry in game.combat_logs:
        for event in turn_entry.get("events", []):
            actor = event.get("caster")
            recipe = event.get("recipe")
            if not recipe:
                continue
            spell_cls = event.get("class", "Unknown")
            if actor == wiz_a.name:
                spells_cast_a[recipe] = spells_cast_a.get(recipe, 0) + 1
                classes_used_a[spell_cls] = classes_used_a.get(spell_cls, 0) + 1
            elif actor == wiz_b.name:
                spells_cast_b[recipe] = spells_cast_b.get(recipe, 0) + 1
                classes_used_b[spell_cls] = classes_used_b.get(spell_cls, 0) + 1

    # Fitness evaluation for backward-compatible telemetry
    w_outcome = 1.0
    w_combo = 1.0
    w_damage = 0.5
    w_entropy = 0.30

    s_combo_a = 0.25 * float(peak_conditions_a)
    s_combo_b = 0.25 * float(peak_conditions_b)
    s_damage_a = (wiz_a.damage_dealt - wiz_a.damage_taken) / 1000.0
    s_damage_b = (wiz_b.damage_dealt - wiz_b.damage_taken) / 1000.0

    def _calc_spell_entropy(spells_dict: Dict[str, int]) -> float:
        total = sum(spells_dict.values())
        if total <= 1:
            return 0.0
        ent = 0.0
        for cnt in spells_dict.values():
            p = cnt / float(total)
            if p > 0:
                ent -= p * math.log(p)
        return ent

    s_entropy_a = _calc_spell_entropy(spells_cast_a)
    s_entropy_b = _calc_spell_entropy(spells_cast_b)

    fitness_a = round(w_outcome * s_outcome_a + w_combo * s_combo_a + w_damage * s_damage_a + w_entropy * s_entropy_a, 4)
    fitness_b = round(w_outcome * s_outcome_b + w_combo * s_combo_b + w_damage * s_damage_b + w_entropy * s_entropy_b, 4)

    # Update Performance Trackers
    def update_bot_stats(
        bot: Dict[str, Any],
        is_winner: bool,
        wiz: Wizard,
        spells_cast: Dict[str, int],
        classes_used: Dict[str, int],
        match_fitness: float,
        peak_conditions: int,
    ):
        tracker = bot.setdefault("performance_tracker", {})
        tracker["matches_played"] = tracker.get("matches_played", 0) + 1
        if is_winner:
            tracker["wins"] = tracker.get("wins", 0) + 1
        else:
            tracker["losses"] = tracker.get("losses", 0) + 1

        matches = tracker["matches_played"]
        tracker["win_rate"] = round(tracker.get("wins", 0) / max(1, matches), 4)
        tracker["damage_dealt"] = round(tracker.get("damage_dealt", 0.0) + wiz.damage_dealt, 1)
        tracker["damage_taken"] = round(tracker.get("damage_taken", 0.0) + wiz.damage_taken, 1)
        tracker["healing_done"] = round(tracker.get("healing_done", 0.0) + wiz.healing_done, 1)
        tracker["turns_survived"] = tracker.get("turns_survived", 0) + game.current_turn

        spell_counts = tracker.setdefault("spell_usage_counts", {})
        for s, c in spells_cast.items():
            spell_counts[s] = spell_counts.get(s, 0) + c

        class_counts = tracker.setdefault("class_usage_counts", {})
        for cls_name, c in classes_used.items():
            class_counts[cls_name] = class_counts.get(cls_name, 0) + c

        tracker["last_match_fitness"] = match_fitness
        tracker["fitness"] = round(tracker.get("fitness", 0.0) + match_fitness, 4)
        tracker["peak_combo_conditions"] = max(tracker.get("peak_combo_conditions", 0), peak_conditions)

    update_bot_stats(bot_a, winner_bot is bot_a, wiz_a, spells_cast_a, classes_used_a, fitness_a, peak_conditions_a)
    update_bot_stats(bot_b, winner_bot is bot_b, wiz_b, spells_cast_b, classes_used_b, fitness_b, peak_conditions_b)

    return {
        "bot_a_id": bot_a["bot_id"],
        "bot_b_id": bot_b["bot_id"],
        "winner_id": winner_bot["bot_id"],
        "loser_id": loser_bot["bot_id"],
        "winner_bot": winner_bot,
        "loser_bot": loser_bot,
        "fitness_a": fitness_a,
        "fitness_b": fitness_b,
        "peak_conditions_a": peak_conditions_a,
        "peak_conditions_b": peak_conditions_b,
        "turns": game.current_turn,
        "p1_final_hp": wiz_a.current_health,
        "p2_final_hp": wiz_b.current_health,
        "result_type": result_type,
    }


# =============================================================================
# 4. SEQUENTIAL PHASE CURRICULUM TRAINING & TOURNAMENT LOOP
# =============================================================================

_GLOBAL_DQN_AGENT: Optional[DQNAgent] = None

def get_global_dqn_agent(
    action_catalog: List[str],
    weights_dict: Optional[Dict[str, Any]] = None,
    reset: bool = False,
    **kwargs,
) -> DQNAgent:
    """
    Maintains a persistent global DQN Agent across tournament iterations,
    preventing replay buffer and optimizer wipes every 50 matches.
    """
    global _GLOBAL_DQN_AGENT
    if _GLOBAL_DQN_AGENT is None or reset:
        _GLOBAL_DQN_AGENT = DQNAgent(
            action_catalog=action_catalog,
            weights_dict=weights_dict,
            **kwargs,
        )
    return _GLOBAL_DQN_AGENT

def reset_global_dqn_agent() -> None:
    """Resets the persistent global DQN Agent."""
    global _GLOBAL_DQN_AGENT
    _GLOBAL_DQN_AGENT = None

def run_tournament_iteration(
    dna_path: Optional[Union[str, Path]] = None,
    spell_data_path: Optional[Union[str, Path]] = None,
    verbose: bool = True,
    board_states: Optional[List[Dict[str, Any]]] = None,
    dqn_agent: Optional[DQNAgent] = None,
    matches_to_play: int = 50,
    eval_mode: bool = False,
    forced_exploration_rate: Optional[float] = None,
    reset_agent: bool = False,
) -> Dict[str, Any]:
    """
    Executes one tournament training iteration using DQN:
    1. Loads bots from ai_bots_dna.json.
    2. Initializes DQN agent with weights from top bot (or existing checkpoint).
    3. Runs matches (50 1v1 duels, standard or curriculum board states), collecting replay experience.
    4. Performs mini-batch DQN training steps on the collected replay buffer.
    5. Updates bot DNA weights and metadata in registry.
    """
    actual_dna_path = resolve_file_path("ai_bots_dna.json", str(dna_path) if dna_path else None)
    actual_spell_path = resolve_file_path("spell_data.json", str(spell_data_path) if spell_data_path else None)

    if not actual_dna_path.exists():
        raise FileNotFoundError(f"AI Bots DNA JSON not found at: {actual_dna_path}")
    if not actual_spell_path.exists():
        raise FileNotFoundError(f"Spell data JSON not found at: {actual_spell_path}")

    with open(actual_dna_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Automatic migration routine for DNA dimensions
    migrated_count = migrate_dna_registry(data)
    if migrated_count > 0 and verbose:
        print(f"[Migration] Automatically migrated {migrated_count} bots to 80-dimensional input layer.")

    bots: List[Dict[str, Any]] = data.get("bots", [])
    if len(bots) < 10:
        raise ValueError(f"Expected at least 10 bots in population, found {len(bots)}.")

    action_catalog = data.get("meta", {}).get("action_catalog")
    if not action_catalog:
        registry = get_registry(str(actual_spell_path))
        action_catalog = registry.all_recipes()

    # Enforce standard wizard stats
    for b in bots:
        b.setdefault("wizard_stats", {
            "starting_hp": 1000.0,
            "base_potency": 100.0,
            "base_defense": 100.0,
            "base_luck": 100.0,
            "base_speed": 100.0,
        })

    # Initialize Persistent DQN Agent if not provided (persists across 50-match iterations)
    if dqn_agent is None:
        best_bot = max(bots, key=lambda b: b.get("performance_tracker", {}).get("win_rate", 0.5))
        dqn_agent = get_global_dqn_agent(
            action_catalog=action_catalog,
            weights_dict=best_bot.get("dna"),
            reset=reset_agent,
        )

    match_results = []
    start_time = time.time()
    if verbose:
        mode_str = "Curriculum Board States" if board_states else "Standard Duels"
        print("\n" + "=" * 75)
        print(f"Starting {matches_to_play} Matches ({mode_str} with {len(bots)} Bots | DQN Agent eps={dqn_agent.epsilon:.3f})")
        print("=" * 75)

    # Matchmaking: Select pairs of bots
    indices = list(range(len(bots)))
    for match_num in range(matches_to_play):
        idx_a = random.choice(indices)
        idx_b = random.choice([i for i in indices if i != idx_a])
        bot_a = bots[idx_a]
        bot_b = bots[idx_b]

        init_state = None
        if board_states:
            if isinstance(board_states, dict):
                init_state = random.choice(list(board_states.values()))
            elif isinstance(board_states, list) and len(board_states) > 0:
                first = board_states[0]
                if isinstance(first, dict) and ("player1" not in first and len(first) > 0):
                    chosen_stage = random.choice(board_states)
                    init_state = random.choice(list(chosen_stage.values()))
                else:
                    init_state = random.choice(board_states)

        result = play_duel(
            bot_a=bot_a,
            bot_b=bot_b,
            action_catalog=action_catalog,
            spell_data_path=str(actual_spell_path),
            max_turns=50,
            initial_board_state=init_state,
            dqn_agent=dqn_agent,
            record_experience=not eval_mode,
            eval_mode=eval_mode,
            forced_exploration_rate=forced_exploration_rate,
        )
        match_results.append(result)

        # Train DQN on mini-batches after each match (only during training mode)
        if not eval_mode and len(dqn_agent.replay_buffer) >= dqn_agent.batch_size:
            for _ in range(2):
                dqn_agent.train_step()

        if verbose:
            print(
                f"Match {match_num + 1:02d}/{matches_to_play}: "
                f"{bot_a.get('bot_id', 'bot_a')} vs {bot_b.get('bot_id', 'bot_b')} "
                f"-> Winner: {result['winner_id']} in {result['turns']} turns | "
                f"Peak Setup: A={result['peak_conditions_a']}, B={result['peak_conditions_b']}"
            )

    elapsed_time = time.time() - start_time
    avg_loss = float(np.mean(dqn_agent.losses[-50:])) if dqn_agent.losses else 0.0

    if verbose:
        print("-" * 75)
        print(f"Completed {matches_to_play} duels in {elapsed_time:.2f}s | "
              f"Replay Size: {len(dqn_agent.replay_buffer)} | "
              f"DQN Loss: {avg_loss:.4f} | Epsilon: {dqn_agent.epsilon:.3f}")

    meta = data.setdefault("meta", {})
    # Synchronize trained DQN weights across population (soft-update top 60%, refresh bottom 40% with diversity noise)
    if not eval_mode:
        cutoff = int(len(bots) * 0.60)
        ranked_bots = sorted(
            bots,
            key=lambda b: b.get("performance_tracker", {}).get("win_rate", 0.5),
            reverse=True,
        )
        for idx_rank, bot in enumerate(ranked_bots):
            if idx_rank < cutoff and "dna" in bot:
                bot_net = QNetwork(weights_dict=bot["dna"])
                bot_net.copy_weights_from(dqn_agent.online_net, tau=0.20)
                bot["dna"] = bot_net.to_dict()
            else:
                mut_net = QNetwork()
                mut_net.copy_weights_from(dqn_agent.online_net, tau=1.0)
                mut_net.w3 += np.random.normal(0.0, 0.015, size=mut_net.w3.shape).astype(np.float32)
                mut_net.b3 += np.random.normal(0.0, 0.01, size=mut_net.b3.shape).astype(np.float32)
                bot["dna"] = mut_net.to_dict()
                bot["generation"] = bot.get("generation", 0) + 1

        # Update metadata
        meta = data.setdefault("meta", {})
        meta["workflow"] = "Deep Q-Network (DQN) Reinforcement Learning & Dynamic Spell Balancing Loop"
        meta["last_trained_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        meta["total_training_iterations"] = meta.get("total_training_iterations", 0) + 1
        meta["total_matches_simulated"] = meta.get("total_matches_simulated", 0) + matches_to_play
        meta["dqn_hyperparameters"] = {
            "learning_rate": dqn_agent.optimizer.lr,
            "gamma": dqn_agent.gamma,
            "epsilon": round(float(dqn_agent.epsilon), 4),
            "epsilon_min": dqn_agent.epsilon_min,
            "epsilon_decay": dqn_agent.epsilon_decay,
            "batch_size": dqn_agent.batch_size,
            "replay_buffer_size": len(dqn_agent.replay_buffer),
            "avg_loss": round(avg_loss, 4),
        }

        # Save updated registry atomically
        temp_dna_path = actual_dna_path.with_suffix(".tmp.json")
        with open(temp_dna_path, "w", encoding="utf-8") as f:
            json.dump(data, f, separators=(",", ":"))
        temp_dna_path.replace(actual_dna_path)

    if verbose:
        print(f"Saved updated DQN models and registry to: {actual_dna_path}\n")

    return {
        "status": "success",
        "matches_played": matches_to_play,
        "replay_buffer_size": len(dqn_agent.replay_buffer),
        "dqn_loss": avg_loss,
        "epsilon": dqn_agent.epsilon,
        "elapsed_seconds": elapsed_time,
        "iteration": meta["total_training_iterations"],
        "dna_path": str(actual_dna_path),
        "results": match_results,
    }


def run_sequential_curriculum_training(
    dna_path: Optional[Union[str, Path]] = None,
    spell_data_path: Optional[Union[str, Path]] = None,
    curriculum_path: Optional[Union[str, Path]] = None,
    matches_per_stage: int = 50,
    verbose: bool = True,
) -> Dict[str, Any]:
    """
    Executes Sequential Phase Curriculum Training across all stages:
      Phase 1: Stage 1 (Immediate finishers / lethal target thresholds)
      Phase 2: Stage 2 (1-turn buffer / single buff setups into payoff)
      Phase 3: Stage 3 (Multi-turn alignment with environmental buffs)
      Phase 4: Stage 4 (Weather/status initiation from clear weather)
      Phase 5: Standard Duels (Full unconstrained 1v1 match play)
    """
    actual_dna_path = resolve_file_path("ai_bots_dna.json", str(dna_path) if dna_path else None)
    actual_spell_path = resolve_file_path("spell_data.json", str(spell_data_path) if spell_data_path else None)

    curr_p = resolve_file_path("training_stages.json", str(curriculum_path) if curriculum_path else None)
    if not curr_p.exists():
        curr_p = resolve_file_path("curriculum_board_states.json", str(curriculum_path) if curriculum_path else None)

    if not curr_p.exists():
        raise FileNotFoundError(f"Curriculum training stages file not found at: {curr_p}")

    with open(curr_p, "r", encoding="utf-8") as f:
        curriculum_data = json.load(f)

    with open(actual_dna_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    action_catalog = data.get("meta", {}).get("action_catalog")
    if not action_catalog:
        registry = get_registry(str(actual_spell_path))
        action_catalog = registry.all_recipes()

    # Instantiate or reuse persistent DQN Agent to preserve replay buffer and weight updates across phases
    best_bot = max(data["bots"], key=lambda b: b.get("performance_tracker", {}).get("win_rate", 0.5))
    if dqn_agent is None:
        dqn_agent = get_global_dqn_agent(
            action_catalog=action_catalog,
            weights_dict=best_bot.get("dna"),
            epsilon=0.8,
            epsilon_min=0.05,
            epsilon_decay=0.996,
        )

    phases = [
        {"name": "Phase 1: Stage 1 Finisher Payoffs", "stage_idx": 1},
        {"name": "Phase 2: Stage 2 Single-Buff Setups", "stage_idx": 2},
        {"name": "Phase 3: Stage 3 Environmental Synergy", "stage_idx": 3},
        {"name": "Phase 4: Stage 4 Match Initiation", "stage_idx": 4},
        {"name": "Phase 5: Full Standard 1v1 Duels", "stage_idx": None},
    ]

    print("\n" + "=" * 80)
    print("PROJECT SORCERY: SEQUENTIAL PHASE CURRICULUM TRAINING (DQN)")
    print(f"Total Phases: 5 | Matches Per Phase: {matches_per_stage} | Total Target Matches: {5 * matches_per_stage}")
    print("=" * 80)

    phase_summaries = []

    for phase in phases:
        st_idx = phase["stage_idx"]
        phase_name = phase["name"]

        board_pool = None
        if st_idx is not None:
            if isinstance(curriculum_data, list) and 1 <= st_idx <= len(curriculum_data):
                stage_obj = curriculum_data[st_idx - 1]
                board_pool = list(stage_obj.values()) if isinstance(stage_obj, dict) else stage_obj
            elif isinstance(curriculum_data, dict):
                st_key = f"stage_{st_idx}" if f"stage_{st_idx}" in curriculum_data else str(st_idx)
                board_pool = list(curriculum_data.get(st_key, {}).values())

        print(f"\n>>> Launching {phase_name} ({matches_per_stage} matches) <<<")
        res = run_tournament_iteration(
            dna_path=actual_dna_path,
            spell_data_path=actual_spell_path,
            verbose=verbose,
            board_states=board_pool,
            dqn_agent=dqn_agent,
            matches_to_play=matches_per_stage,
        )

        phase_summaries.append({
            "phase": phase_name,
            "stage": st_idx,
            "loss": res["dqn_loss"],
            "epsilon": res["epsilon"],
            "replay_size": res["replay_buffer_size"],
            "elapsed_seconds": res["elapsed_seconds"],
        })

    print("\n" + "=" * 80)
    print("SEQUENTIAL CURRICULUM COMPLETE - SUMMARY OF PHASES")
    print("=" * 80)
    for s in phase_summaries:
        print(f"• {s['phase']:<42} | Loss: {s['loss']:.4f} | Epsilon: {s['epsilon']:.3f} | Replay: {s['replay_size']}")
    print("=" * 80 + "\n")

    return {
        "status": "success",
        "phases_completed": len(phases),
        "total_matches": 5 * matches_per_stage,
        "final_epsilon": dqn_agent.epsilon,
        "replay_buffer_size": len(dqn_agent.replay_buffer),
        "phase_summaries": phase_summaries,
    }


def main(
    dna_path: Optional[Union[str, Path]] = None,
    spell_data_path: Optional[Union[str, Path]] = None,
    verbose: bool = True,
    board_states: Optional[List[Dict[str, Any]]] = None,
    sequential_curriculum: bool = False,
    matches_per_stage: int = 50,
    dqn_agent: Optional[DQNAgent] = None,
    eval_mode: bool = False,
    forced_exploration_rate: Optional[float] = None,
    reset_agent: bool = False,
) -> Dict[str, Any]:
    """Main entry point for simulation suite."""
    if sequential_curriculum:
        return run_sequential_curriculum_training(
            dna_path=dna_path,
            spell_data_path=spell_data_path,
            matches_per_stage=matches_per_stage,
            verbose=verbose,
            dqn_agent=dqn_agent,
        )
    else:
        return run_tournament_iteration(
            dna_path=dna_path,
            spell_data_path=spell_data_path,
            verbose=verbose,
            board_states=board_states,
            dqn_agent=dqn_agent,
            matches_to_play=matches_per_stage,
            eval_mode=eval_mode,
            forced_exploration_rate=forced_exploration_rate,
            reset_agent=reset_agent,
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Project Sorcery AI Bot Deep Q-Network (DQN) Runner")
    parser.add_argument("--dna", type=str, default=None, help="Path to ai_bots_dna.json")
    parser.add_argument("--spells", type=str, default=None, help="Path to spell_data.json")
    parser.add_argument("--iterations", type=int, default=1, help="Number of iterations to run (default: 1)")
    parser.add_argument("--curriculum", type=str, default=None, help="Path to training_stages.json")
    parser.add_argument("--stage", type=int, default=None, choices=[1, 2, 3, 4], help="Stage of curriculum to sample from (1..4)")
    parser.add_argument("--sequential-curriculum", action="store_true", help="Run full sequential phase curriculum (Stages 1->2->3->4->Full)")
    parser.add_argument("--matches-per-stage", type=int, default=50, help="Matches per curriculum stage (default: 50)")
    parser.add_argument("--eval-mode", action="store_true", help="Run in evaluation mode without training updates")
    parser.add_argument("--forced-exploration-rate", type=float, default=None, help="Forced exploration rate during action selection (e.g. 0.08 for ~200 casts per spell)")
    parser.add_argument("--reset-agent", action="store_true", help="Reset persistent DQN agent instead of reusing across iterations")
    parser.add_argument("--quiet", action="store_true", help="Suppress verbose match logging")

    args = parser.parse_args()

    if args.sequential_curriculum:
        main(
            dna_path=args.dna,
            spell_data_path=args.spells,
            verbose=not args.quiet,
            sequential_curriculum=True,
            matches_per_stage=args.matches_per_stage,
        )
    else:
        board_states_pool = None
        curr_p = resolve_file_path("training_stages.json", args.curriculum)
        if not curr_p.exists():
            curr_p = resolve_file_path("curriculum_board_states.json", args.curriculum)

        if curr_p.exists() and (args.curriculum or args.stage is not None):
            with open(curr_p, "r", encoding="utf-8") as f:
                c_data = json.load(f)
            if isinstance(c_data, list):
                if args.stage is not None and 1 <= args.stage <= len(c_data):
                    board_states_pool = list(c_data[args.stage - 1].values())
                else:
                    board_states_pool = c_data
            elif isinstance(c_data, dict):
                if args.stage is not None:
                    st_key = f"stage_{args.stage}" if f"stage_{args.stage}" in c_data else str(args.stage)
                    board_states_pool = list(c_data.get(st_key, {}).values())
                else:
                    board_states_pool = c_data

        for i in range(args.iterations):
            if args.iterations > 1:
                print(f"\n>>> Running Iteration {i+1} of {args.iterations} <<<")
            main(
                dna_path=args.dna,
                spell_data_path=args.spells,
                verbose=not args.quiet,
                board_states=board_states_pool,
            )
