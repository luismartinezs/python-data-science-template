import pandas as pd
import numpy as np

# Read the CSV file
df = pd.read_csv('choices.csv')

# Calculate the product of probability and outcome for each row
df['value'] = df['prob'] * df['outcome']

# Calculate expected values by grouping by project and summing the 'value'
expected_values = df.groupby('project')['value'].sum()

# Calculate sum of probabilities per project
prob_sums = df.groupby('project')['prob'].sum()

# Print the expected values for each project using header info for labels
print("Expected Value per Project:")
for project_name, ev in expected_values.items():
    print(f"Project {project_name}: {ev:,.0f}")

print("\\nProbability Sum per Project:")
for project_name, prob_sum in prob_sums.items():
    print(f"Project {project_name}: {prob_sum:.2f}")
    # Check if probabilities sum to 1 (within a small tolerance for floating point errors)
    if not np.isclose(prob_sum, 1.0):
        print(f"  WARNING: Probabilities for Project {project_name} do not sum to 1!")

winner = expected_values.idxmax()
print(f"\nRecommended choice: {winner} (EV = {expected_values[winner]:,.0f})")
