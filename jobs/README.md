Perfect — you’re asking:

> If we start with **N human jobs**, and then AI:

* **automates (100 – Y)%** of those jobs (so only **Y% remain** for humans),
* **creates X% more new jobs** in total,

**how many human jobs remain** at timestamp 2? And how does that compare to the original N?

---

### Variables:

* `N` = original number of jobs (all human)
* `Y` = % of jobs that still require a human (e.g. 60 means 60% still need humans)
* `X` = % increase in total jobs due to AI (e.g. 20 means 20% more total jobs)

---

### Step-by-step:

1. **Total jobs after AI**:

   $$
   N_{\text{after}} = N \times \left(1 + \frac{X}{100}\right)
   $$

2. **Human jobs after AI**:

   $$
   H_{\text{after}} = N_{\text{after}} \times \frac{Y}{100}
   = N \times \left(1 + \frac{X}{100}\right) \times \frac{Y}{100}
   $$

3. **Ratio of human jobs before vs after**:

   $$
   \text{Ratio} = \frac{H_{\text{after}}}{N}
   = \left(1 + \frac{X}{100}\right) \times \frac{Y}{100}
   $$

---

### Example:

Suppose:

* `N = 100`
* `X = 20` (20% more jobs)
* `Y = 50` (only 50% of jobs still need humans)

Then:

* Total jobs after AI: `100 × 1.2 = 120`
* Human jobs after AI: `120 × 0.5 = 60`
* Compared to original: `60 / 100 = 0.6` → **40% reduction** in human jobs

---

### Summary Formula:

$$
\boxed{
\text{New human jobs} = N \times \left(1 + \frac{X}{100}\right) \times \frac{Y}{100}
}
$$

You can plug in your values to get the exact number or percentage change. Let me know if you'd like a calculator function or plot for this.
