# Multi-Agent Grid Coverage with PPO

This example demonstrates using three PPO agents to collaboratively explore and achieve full coverage of a grid-world environment.

## Environment Setup

The environment consists of:
- An NxN grid world
- Three PPO agents starting at random positions
- Each cell can be either unexplored or explored
- Agents can move in 4 directions (up, down, left, right)
- Agents receive observations of:
  - Their current position
  - Local view of explored/unexplored cells
  - Other agents' positions within view range

## Reward Structure

Agents receive rewards for:
- Exploring new cells (+1 per new cell)
- Maintaining distance from other agents (+0.2 for good spacing)
- Reaching full coverage (+10 bonus)
- Small negative reward per timestep (-0.1) to encourage efficiency

## PPO Implementation

Each agent uses PPO with:
- Actor-critic architecture
- Shared policy network for all agents
- Local observations as input
- Discrete action space (4 directions)
- Value function estimating expected returns
- Clipped surrogate objective
- Entropy bonus for exploration

## Training Process

1. Initialize environment and 3 PPO agents
2. For each episode:
   - Reset environment
   - Until coverage complete or max steps:
     - Each agent:
       - Observe local state
       - Sample action from policy
       - Execute action
       - Store (state, action, reward) tuple
   - Update policies using PPO algorithm
   - Track coverage metrics

The agents learn to coordinate their exploration while maintaining efficient spacing, ultimately achieving full grid coverage through emergent cooperative behavior.
