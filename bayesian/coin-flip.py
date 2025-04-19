import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# -----------------------
# 1. Pretend data arrives
# -----------------------
data = np.random.choice([1, 0], size=20)  # 1=heads, 0=tails

# -----------------------
# 2. Choose prior
# -----------------------
alpha, beta_param = 1, 1                  # Beta(1,1) ~ "completely agnostic"

posterior_means, ci_low, ci_high = [], [], []

for i, flip in enumerate(data, 1):
    # 3. Update pseudo-counts
    alpha      += flip
    beta_param += 1 - flip

    # 4. Store diagnostics
    pm = alpha / (alpha + beta_param)
    posterior_means.append(pm)

    # 95 % credible interval
    ci_low.append(beta.ppf(0.025, alpha, beta_param))
    ci_high.append(beta.ppf(0.975, alpha, beta_param))

# -----------------------
# 5. Visualise learning
# -----------------------
x = np.arange(1, len(data)+1)
plt.fill_between(x, ci_low, ci_high, alpha=0.3, label='95% credible interval')
plt.plot(x, posterior_means, marker='o', label='posterior mean')
plt.xlabel('Flip #')
plt.ylabel('P(heads)')
plt.title('Bayesian learning in action')
plt.ylim(0, 1)
plt.legend()
plt.tight_layout()
plt.savefig('posterior_coin.png')   # deliverable for your checkpoint
plt.show()
