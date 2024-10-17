import numpy as np


# Environment definition
class InfluencerAppEnvironment:
    def __init__(self, initial_time=14):
        self.time_remaining = initial_time  # 14 days to achieve the goal
        self.development_progress = 0  # % of app development completed
        self.revenue_generated = 0  # Initial revenue
        self.user_feedback = 0  # Engagement from influencers
        self.revenue_goal = 500  # Revenue target

    # Simulate state transition based on action
    def step(self, action):
        reward = 0
        if action == "work_on_core":
            # Increase development progress
            self.development_progress += np.random.uniform(0.1, 0.3)
            reward += 1  # Progress reward
        elif action == "build_marketing_page":
            # Minor progress but setup for outreach
            reward += 0.5
        elif action == "reach_out_to_influencers":
            if self.development_progress >= 0.7:  # Need core app mostly done
                self.user_feedback += np.random.uniform(0, 1)
                reward += 2 if self.user_feedback > 0.5 else 0  # Good feedback
        elif action == "gather_feedback":
            if self.user_feedback > 0:
                # Feedback helps improve the product or increase engagement
                reward += np.random.uniform(0, 1)

        # Time passes, negative reward for time wasted
        self.time_remaining -= 1
        if self.time_remaining <= 0:
            reward -= 10  # Penalty for running out of time

        # Check if revenue goal is achieved
        self.revenue_generated = self.user_feedback * 100  # Simplified revenue model
        if self.revenue_generated >= self.revenue_goal:
            reward += 20  # Reward for hitting the goal

        return reward, self.get_state(), self.time_remaining <= 0

    def get_state(self):
        return (
            self.development_progress,
            self.user_feedback,
            self.revenue_generated,
            self.time_remaining,
        )


# Actions: work on core, build marketing, reach out, gather feedback
actions = [
    "work_on_core",
    "build_marketing_page",
    "reach_out_to_influencers",
    "gather_feedback",
]


# Initial policy based on heuristic (simple decision tree)
def choose_action(state):
    development_progress, user_feedback, revenue, time_remaining = state
    if development_progress < 0.7:
        return "work_on_core"
    elif user_feedback < 0.3:
        return "reach_out_to_influencers"
    elif revenue < 500 and user_feedback > 0.3:
        return "gather_feedback"
    else:
        return "build_marketing_page"


# Simulate agent's decisions
env = InfluencerAppEnvironment()
for _ in range(14):  # 14 days simulation
    current_state = env.get_state()
    action = choose_action(current_state)
    reward, new_state, done = env.step(action)
    print(f"Action: {action}, Reward: {reward}, New State: {new_state}")
    if done:
        print("Simulation complete. Goal achieved!")
        break
