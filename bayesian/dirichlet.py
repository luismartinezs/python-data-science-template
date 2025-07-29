import numpy as np
from scipy.stats import dirichlet

presses = ['A', 'C', 'A', 'B']
counts  = {'A':1, 'B':1, 'C':1}        # Dirichlet(1,1,1) prior

for p in presses:
    counts[p] += 1                      # add‑1 update

tot = sum(counts.values())
posterior_mean = {k: v/tot for k, v in counts.items()}
print("Counts:", counts)
print("Posterior mean:", posterior_mean)
