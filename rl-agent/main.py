import numpy as np


# Example: Random probabilistic response from the environment
def environment_response(action_params):
    # Example: Action impacts (could be probabilistic, or rule-based)
    cost_reduction = np.random.normal(
        loc=action_params["cost_reduction_mean"],
        scale=action_params["cost_reduction_std"],
    )
    time_reduction = np.random.normal(
        loc=action_params["time_reduction_mean"],
        scale=action_params["time_reduction_std"],
    )

    # Simulate uncertainty in environment (e.g., random failure rate)
    success_chance = np.random.uniform(0, 1)
    is_successful = success_chance < action_params["success_rate"]

    return {
        "cost_reduction": cost_reduction,
        "time_reduction": time_reduction,
        "is_successful": is_successful,
    }


def agent_action(strategy):
    # The agent adjusts its strategy and sends actions to the environment
    action_params = {
        "cost_reduction_mean": strategy["cost_factor"],
        "cost_reduction_std": strategy["cost_uncertainty"],
        "time_reduction_mean": strategy["time_factor"],
        "time_reduction_std": strategy["time_uncertainty"],
        "success_rate": strategy["success_rate"],
    }
    return action_params


def simulate_strategy(strategy, iterations=1000):
    total_reward = 0
    for i in range(iterations):
        # Agent takes an action (sends strategy to the environment)
        action_params = agent_action(strategy)

        # Environment responds
        response = environment_response(action_params)

        # Reward is calculated based on cost, time and success
        if response["is_successful"]:
            reward = response["cost_reduction"] + response["time_reduction"]
        else:
            reward = -100  # Penalty for failure

        total_reward += reward

    average_reward = total_reward / iterations
    return average_reward


strategies = [
    {
        "cost_factor": 10,
        "cost_uncertainty": 2,
        "time_factor": 5,
        "time_uncertainty": 1,
        "success_rate": 0.9,
    },
    {
        "cost_factor": 50,
        "cost_uncertainty": 10,
        "time_factor": 50,
        "time_uncertainty": 10,
        "success_rate": 0.9,
    },
]

# Run simulations for each strategy
for strategy in strategies:
    avg_reward = simulate_strategy(strategy)
    print(f"Strategy {strategy} => Average Reward: {avg_reward}")
