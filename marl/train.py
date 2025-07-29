import numpy as np
from env import GridCoverageEnv
from ppo import PPOAgent
from typing import List, Dict, Tuple
import torch


def compute_returns_and_advantages(
    rewards: List[float],
    values: List[float],
    gamma: float = 0.99,
    lambda_: float = 0.95,
) -> Tuple[List[float], List[float]]:
    returns = []
    advantages = []
    next_value = 0
    next_advantage = 0

    for r, v in zip(reversed(rewards), reversed(values)):
        returns.insert(0, r + gamma * next_value)
        delta = r + gamma * next_value - v
        advantages.insert(0, delta + gamma * lambda_ * next_advantage)
        next_value = v
        next_advantage = advantages[0]

    return returns, advantages


def train(n_episodes: int = 1000, grid_size: int = 10, n_agents: int = 3):
    env = GridCoverageEnv(grid_size=grid_size, n_agents=n_agents)
    agents = [
        PPOAgent(env.observation_space.shape[0], env.action_space.n)
        for _ in range(n_agents)
    ]

    for episode in range(n_episodes):
        states, actions, rewards, probs, values = [], [], [], [], []
        obs, _ = env.reset()
        done = False
        episode_reward = 0

        while not done:
            # Collect experience
            episode_actions = []
            episode_probs = []
            episode_values = []

            for i, agent in enumerate(agents):
                action, prob, value = agent.select_action(obs[i])
                episode_actions.append(action)
                episode_probs.append(prob)
                episode_values.append(value)

            next_obs, step_rewards, done, _, _ = env.step(episode_actions)

            # Store experience
            states.append(obs)
            actions.append(episode_actions)
            rewards.append(step_rewards)
            probs.append(episode_probs)
            values.append(episode_values)

            obs = next_obs
            episode_reward += sum(step_rewards)

        # Prepare batch for each agent
        for i in range(n_agents):
            agent_states = [s[i] for s in states]
            agent_actions = [a[i] for a in actions]
            agent_rewards = [r[i] for r in rewards]
            agent_probs = [p[i] for p in probs]
            agent_values = [v[i] for v in values]

            # Compute returns and advantages
            returns, advantages = compute_returns_and_advantages(
                agent_rewards, agent_values
            )

            # Normalize advantages
            advantages = (advantages - np.mean(advantages)) / (
                np.std(advantages) + 1e-8
            )

            # Update agent
            batch = {
                "states": agent_states,
                "actions": agent_actions,
                "returns": returns,
                "advantages": advantages,
                "probs": agent_probs,
            }

            agents[i].update(batch)

        if (episode + 1) % 10 == 0:
            print(
                f"Episode {episode + 1}, Average Reward: {episode_reward / len(rewards):.2f}"
            )


if __name__ == "__main__":
    train()
