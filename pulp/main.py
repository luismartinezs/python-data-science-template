from pulp import LpProblem, LpMaximize, LpVariable, lpSum

# Define the problem
prob = LpProblem("Product Mix Problem", LpMaximize)

# Define decision variables
x1 = LpVariable("Product_1", lowBound=0, cat="Integer")
x2 = LpVariable("Product_2", lowBound=0, cat="Integer")

# Define the objective function
prob += 40 * x1 + 50 * x2, "Profit"

# Define constraints
prob += 2 * x1 + 3 * x2 <= 100, "Labor_hours"
prob += x1 + x2 <= 50, "Raw_materials"

# Solve the problem
prob.solve()

# Print the results
print("Status:", prob.status)
print("Optimal Production Plan:")
print("Product 1:", x1.varValue)
print("Product 2:", x2.varValue)
print("Total Profit: $", prob.objective.value())

# Sensitivity Analysis
for name, constraint in prob.constraints.items():
    print(f"{name} Shadow Price: {constraint.pi}")
    print(f"{name} Slack: {constraint.slack}")
