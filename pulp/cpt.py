from pulp import LpProblem, LpMinimize, LpVariable, lpSum

# Task durations
durations = {"A": 4, "B": 2, "C": 6, "D": 1, "E": 3, "F": 5}

# Define problem
prob = LpProblem("Critical Path", LpMinimize)

# Create a variable for the start time of each task
start_times = {task: LpVariable(f"start_{task}", lowBound=0) for task in durations}

# Objective: minimize the end time of the last task 'F'
prob += start_times["F"] + durations["F"]

# Add constraints for dependencies
prob += start_times["B"] >= start_times["A"] + durations["A"]
prob += start_times["C"] >= start_times["A"] + durations["A"]
prob += start_times["D"] >= start_times["B"] + durations["B"]
prob += start_times["E"] >= start_times["C"] + durations["C"]
prob += start_times["F"] >= start_times["D"] + durations["D"]
prob += start_times["F"] >= start_times["E"] + durations["E"]

# Solve the problem
prob.solve()

# Output results
for task in durations:
    print(f"Start time for task {task}: {start_times[task].varValue}")
