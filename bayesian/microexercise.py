import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt

a, b = 1, 1

data = np.random.choice([1, 0], size=20)

posterior_means, ci_low, ci_high = [], [], []

for i, flip in enumerate(data, 1):
    a += flip
    b += 1 - flip

    pm = a / (a + b)
    posterior_means.append(pm)

    ci_low.append(beta.ppf(0.025, a, b))
    ci_high.append(beta.ppf(0.975, a, b))

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