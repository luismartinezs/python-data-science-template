import numpy as np
from scipy.stats import dirichlet

print("\n=== Bayesian Learning with Dirichlet Distribution ===")

# Step 1: Set prior
print("\nStep 1: Setting prior parameters...")
prior = np.array([1, 1, 1])  # Dirichlet(1,1,1)
labels = ['A', 'B', 'C']
label_to_index = {label: i for i, label in enumerate(labels)}
print(f"Prior parameters (alpha): {prior}")
print(f"Labels: {labels}")

# Step 2: Generate synthetic data
print("\nStep 2: Generating synthetic data...")
true_probs = [0.6, 0.25, 0.15]
data = np.random.choice(labels, size=10_000, p=true_probs)
print(f"Generated {len(data)} observations with true probabilities:")
for label, p in zip(labels, true_probs):
    print(f"P({label}) = {p:.2f}")

# Step 3: Start updating and check convergence
print("\nStep 3: Updating counts and checking confidence threshold...")
threshold = 0.05
alpha = prior.copy()
stop_at = None

for i, obs in enumerate(data, 1):  # i = 1 to N
    idx = label_to_index[obs]
    alpha[idx] += 1

    # Sample from updated Dirichlet
    samples = dirichlet.rvs(alpha, size=5000)
    ci_low = np.percentile(samples, 2.5, axis=0)
    ci_high = np.percentile(samples, 97.5, axis=0)
    widths = ci_high - ci_low

    if np.all(widths < 2 * threshold):
        stop_at = i
        break

# Step 4: Results
if stop_at:
    print(f"\n✅ Converged after {stop_at} observations (95% CI width < ±{threshold})")
    posterior_mean = dirichlet.mean(alpha)
    print("\nPosterior Summary:")
    for i, label in enumerate(labels):
        print(f"{label}:")
        print(f"  Count           = {alpha[i]}")
        print(f"  Posterior Mean  = {posterior_mean[i]:.3f}")
        print(f"  95% CI          = [{ci_low[i]:.3f}, {ci_high[i]:.3f}] (width = {(ci_high[i] - ci_low[i]):.3f})")
else:
    print("\n❌ Did not reach the confidence threshold within the data stream.")
