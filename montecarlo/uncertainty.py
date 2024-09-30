import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr


# Function to calculate mu and sigma for lognormal distribution
def calculate_lognormal_params(mean, std_dev):
    mu = np.log(mean**2 / np.sqrt(std_dev**2 + mean**2))
    sigma = np.sqrt(np.log(1 + (std_dev**2 / mean**2)))
    return mu, sigma


# Number of simulations
num_simulations = 10000

# Market competition: normal - fraction of market captured (0 to 1)
X1 = np.random.normal(loc=0.5, scale=0.3, size=num_simulations)
X1 = np.clip(X1, 0, 1)  # Competition must be between 0 and 1

# Market size: log-normal - peak = 1000, std_dev = 800
mu, sigma = calculate_lognormal_params(1000, 800)
X2 = np.random.lognormal(mu, sigma, size=num_simulations)

# Price per customer
mu, sigma = calculate_lognormal_params(20, 10)
X3 = np.random.lognormal(mu, sigma, size=num_simulations)

# other distributions: uniform, triangular, ...


# Simulation function: total revenue
def simulation(X1, X2, X3):
    return X1 * X2 * X3


# Run the simulation
results = simulation(X1, X2, X3)

# Analyze the results
mean_result = np.mean(results)
std_result = np.std(results)
percentiles = np.percentile(results, [5, 50, 95])

# Output basic stats
print(f"Mean of results: {mean_result}")
print(f"Standard deviation of results: {std_result}")
print(f"5th, 50th, 95th percentiles: {percentiles}")

# Define a threshold for "failure"
failure_threshold = 500
failure_probability = np.mean(results < failure_threshold)
print(
    f"Probability of failure (result < {failure_threshold}): {failure_probability * 100:.2f}%"
)
print(
    f"Probability of success (result > {failure_threshold}): {(1 - failure_probability) * 100:.2f}%"
)

# Sensitivity analysis (correlation between inputs and result)
corr_X1, _ = pearsonr(X1, results)
corr_X2, _ = pearsonr(X2, results)
corr_X3, _ = pearsonr(X3, results)
print(f"Correlation between X1 (market competition) and result: {corr_X1:.2f}")
print(f"Correlation between X2 (market size) and result: {corr_X2:.2f}")
print(f"Correlation between X3 (price per customer) and result: {corr_X3:.2f}")

# Plot the results
plt.hist(results, bins=50, edgecolor="k", alpha=0.7)
plt.title("Monte Carlo Simulation Results")
plt.xlabel("Result")
plt.ylabel("Frequency")
plt.show()
