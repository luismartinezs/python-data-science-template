import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 10000  # baseline number of jobs
X_values = np.linspace(0, 100, 500)  # X varies from 0% to 100% increase in jobs

# Fixed Y percentages for different curves (in %)
Y_values = [20, 40, 60, 80, 100]

plt.figure(figsize=(10, 6))

for Y in Y_values:
    # Compute the number of human jobs at timestamp 2 for each value of X.
    # Formula: new_human_jobs = N * (1 + X/100) * (Y/100)
    human_jobs = N * (1 + X_values/100) * (Y/100)
    plt.plot(X_values, human_jobs, label=f'Y = {Y}%')

plt.xlabel('X (%) - Percentage Increase in Total Jobs Due to AI')
plt.ylabel('Number of Human Jobs')
plt.title('Number of Human Jobs After AI Creation\nN=10,000, varying X and fixed values of Y')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
