import numpy as np
import matplotlib.pyplot as plt

# Number of simulations
num_simulations = 10000

# Define distributions for X1, X2, X3, X4
# X1 ~ Normal(10, 2)
X1 = np.random.normal(loc=10, scale=2, size=num_simulations)

# X2 ~ Uniform(5, 15)
X2 = np.random.uniform(low=5, high=15, size=num_simulations)

# X3 ~ Triangular(1, 3, 10)
X3 = np.random.triangular(left=1, mode=3, right=10, size=num_simulations)

# X4 ~ Log-Normal(mean=0, sigma=0.25)
X4 = np.random.lognormal(mean=0, sigma=0.25, size=num_simulations)


# Define the function f(X1, X2, X3, X4) = X1 + X2 * X3 - X4
def simulation(X1, X2, X3, X4):
    return X1 + X2 * X3 - X4


# Run the simulation
results = simulation(X1, X2, X3, X4)

# Analyze the results: mean, std, percentiles, etc.
mean_result = np.mean(results)
std_result = np.std(results)
percentiles = np.percentile(results, [5, 50, 95])

print(f"Mean of results: {mean_result}")
print(f"Standard deviation of results: {std_result}")
print(f"5th, 50th, 95th percentiles: {percentiles}")

# Plot the results
plt.hist(results, bins=50, edgecolor="k", alpha=0.7)
plt.title("Monte Carlo Simulation Results")
plt.xlabel("Result")
plt.ylabel("Frequency")
plt.show()
