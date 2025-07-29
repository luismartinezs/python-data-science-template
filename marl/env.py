import numpy as np
import gymnasium as gym
from gymnasium import spaces
from typing import List, Tuple, Dict


class GridCoverageEnv(gym.Env):
    def __init__(self, grid_size: int = 10, n_agents: int = 3, view_range: int = 3):
        super().__init__()
        self.grid_size = grid_size
        self.n_agents = n_agents
        self.view_range = view_range

        # Spaces
        self.action_space = spaces.Discrete(4)  # up, down, left, right

        # Observation: local view (2*view_range+1)^2 + 2 (position) + 2*n_agents (other agents positions)
        obs_size = (2 * view_range + 1) ** 2 + 2 + 2 * (n_agents - 1)
        self.observation_space = spaces.Box(
            low=0, high=1, shape=(obs_size,), dtype=np.float32
        )

        self.reset()

    def reset(self, seed=None):
        super().reset(seed=seed)
        self.grid = np.zeros(
            (self.grid_size, self.grid_size)
        )  # 0: unexplored, 1: explored
        self.agent_positions = self._initialize_agents()
        self.steps = 0
        return self._get_observations(), {}

    def _initialize_agents(self) -> List[Tuple[int, int]]:
        positions = []
        while len(positions) < self.n_agents:
            pos = (
                np.random.randint(0, self.grid_size),
                np.random.randint(0, self.grid_size),
            )
            if pos not in positions:
                positions.append(pos)
        return positions

    def _get_observations(self) -> List[np.ndarray]:
        observations = []
        for i, pos in enumerate(self.agent_positions):
            obs = self._get_agent_observation(i)
            observations.append(obs)
        return observations

    def _get_agent_observation(self, agent_idx: int) -> np.ndarray:
        x, y = self.agent_positions[agent_idx]

        # Get local view
        local_view = np.zeros((2 * self.view_range + 1, 2 * self.view_range + 1))
        for i in range(-self.view_range, self.view_range + 1):
            for j in range(-self.view_range, self.view_range + 1):
                if 0 <= x + i < self.grid_size and 0 <= y + j < self.grid_size:
                    local_view[i + self.view_range, j + self.view_range] = self.grid[
                        x + i, y + j
                    ]

        # Flatten local view
        obs = local_view.flatten()

        # Add agent's position
        obs = np.append(obs, [x / self.grid_size, y / self.grid_size])

        # Add other agents' positions
        for i in range(self.n_agents):
            if i != agent_idx:
                ax, ay = self.agent_positions[i]
                obs = np.append(obs, [ax / self.grid_size, ay / self.grid_size])

        return obs.astype(np.float32)

    def step(self, actions: List[int]):
        self.steps += 1
        rewards = []

        # Move agents and compute rewards
        for i, action in enumerate(actions):
            reward = self._move_agent(i, action)
            rewards.append(reward)

        # Check if episode is done
        done = np.all(self.grid == 1) or self.steps >= self.grid_size * self.grid_size

        return self._get_observations(), rewards, done, done, {}

    def _move_agent(self, agent_idx: int, action: int) -> float:
        x, y = self.agent_positions[agent_idx]

        # Move agent
        if action == 0:  # up
            x = max(0, x - 1)
        elif action == 1:  # down
            x = min(self.grid_size - 1, x + 1)
        elif action == 2:  # left
            y = max(0, y - 1)
        elif action == 3:  # right
            y = min(self.grid_size - 1, y + 1)

        self.agent_positions[agent_idx] = (x, y)

        # Compute reward
        reward = -0.1  # Step penalty

        # Reward for exploring new cell
        if self.grid[x, y] == 0:
            reward += 1
            self.grid[x, y] = 1

        # Reward for maintaining distance from other agents
        for j in range(self.n_agents):
            if j != agent_idx:
                dist = np.sqrt(
                    (x - self.agent_positions[j][0]) ** 2
                    + (y - self.agent_positions[j][1]) ** 2
                )
                if dist >= self.view_range:
                    reward += 0.2

        # Bonus for full coverage
        if np.all(self.grid == 1):
            reward += 10

        return reward
