# montecarlo.py  --runs 10000 assumptions.yaml
import sys, yaml, json, pathlib, numpy as np, pandas as pd, matplotlib.pyplot as plt

runs      = int(sys.argv[sys.argv.index('--runs') + 1])
params    = yaml.safe_load(open(sys.argv[-1]))
months    = 1

# 1. Correlated shocks ---------------------------------------------------------
mu   = np.array(params['mu'])               # e.g. [0, 0] for demand & price
cov  = np.array(params['corr']) * np.outer(params['sigma'], params['sigma'])
z    = np.random.default_rng().multivariate_normal(mu, cov, size=runs)

# 2. Transform to real-world drivers ------------------------------------------
demand = params['base_demand'] * np.exp(z[:,0])        # log-normal
price  = params['base_price']  * np.exp(z[:,1])

# 3. Revenue per sample --------------------------------------------------------
rev = (demand * price * months).round(2)

# 4. Persist artefacts ---------------------------------------------------------
stats = {
    'mean': float(rev.mean()),
    'std':  float(rev.std()),
    'p05':  float(np.percentile(rev, 5)),
    'p95':  float(np.percentile(rev, 95))
}
pathlib.Path('rev_stats.json').write_text(json.dumps(stats, indent=2))

plt.hist(rev, bins=50)
plt.title('12-month Revenue Distribution')
plt.xlabel('Revenue'); plt.ylabel('Frequency')
plt.savefig('rev_hist.png', dpi=150)

print('Saved rev_hist.png and rev_stats.json')