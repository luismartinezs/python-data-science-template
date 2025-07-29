import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from typing import List, Tuple


class PPONetwork(nn.Module):
    def __init__(self, obs_dim: int, action_dim: int):
        super().__init__()

        # Shared features
        self.features = nn.Sequential(
            nn.Linear(obs_dim, 64), nn.ReLU(), nn.Linear(64, 64), nn.ReLU()
        )

        # Policy head
        self.policy = nn.Sequential(nn.Linear(64, action_dim), nn.Softmax(dim=-1))

        # Value head
        self.value = nn.Sequential(nn.Linear(64, 1))

    def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        features = self.features(x)
        return self.policy(features), self.value(features)


class PPOAgent:
    def __init__(self, obs_dim: int, action_dim: int, lr: float = 3e-4):
        self.network = PPONetwork(obs_dim, action_dim)
        self.optimizer = optim.Adam(self.network.parameters(), lr=lr)

        self.clip_param = 0.2
        self.value_coef = 0.5
        self.entropy_coef = 0.01

    def select_action(self, obs: np.ndarray) -> Tuple[int, float, float]:
        with torch.no_grad():
            obs = torch.FloatTensor(obs)
            probs, value = self.network(obs)
            action = torch.multinomial(probs, 1).item()
            return action, probs[action].item(), value.item()

    def update(self, batch: dict) -> dict:
        states = torch.FloatTensor(batch["states"])
        actions = torch.LongTensor(batch["actions"])
        old_probs = torch.FloatTensor(batch["probs"])
        returns = torch.FloatTensor(batch["returns"])
        advantages = torch.FloatTensor(batch["advantages"])

        # Get current policy and value predictions
        probs, values = self.network(states)
        curr_probs = probs.gather(1, actions.unsqueeze(1)).squeeze()

        # Policy loss
        ratio = curr_probs / old_probs
        surr1 = ratio * advantages
        surr2 = (
            torch.clamp(ratio, 1 - self.clip_param, 1 + self.clip_param) * advantages
        )
        policy_loss = -torch.min(surr1, surr2).mean()

        # Value loss
        value_loss = 0.5 * (returns - values.squeeze()).pow(2).mean()

        # Entropy bonus
        entropy = -(probs * torch.log(probs + 1e-10)).sum(dim=-1).mean()

        # Total loss
        loss = policy_loss + self.value_coef * value_loss - self.entropy_coef * entropy

        # Update network
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        return {
            "policy_loss": policy_loss.item(),
            "value_loss": value_loss.item(),
            "entropy": entropy.item(),
        }
