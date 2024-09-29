# Note this is wrong
import networkx as nx
import matplotlib.pyplot as plt

# Create a Directed Acyclic Graph (DAG)
G = nx.DiGraph()

# Define task labels
task_labels = [
    "do task A",  # 0
    "do task B",  # 1
    "do task C",  # 2
    "do task D",  # 3
    "do task E",  # 4
    "do task F",  # 5
    "do task G",  # 6
    "do task H",  # 7
    "do task I",  # 8
    "do task J",  # 9
    "do task K",  # 10
    "do task L",  # 11
    "do task M",  # 12
]

# Add tasks (nodes) and their durations
tasks = {
    label: duration
    for label, duration in zip(task_labels, [4, 2, 6, 1, 3, 5, 3, 4, 2, 5, 3, 4, 2])
}

# Add dependencies (edges), where (task1, task2) means task2 depends on task1
dependencies = [
    (task_labels[0], task_labels[1]),
    (task_labels[0], task_labels[2]),
    (task_labels[0], task_labels[3]),
    (task_labels[1], task_labels[4]),
    (task_labels[1], task_labels[5]),
    (task_labels[2], task_labels[6]),
    (task_labels[2], task_labels[7]),
    (task_labels[3], task_labels[8]),
    (task_labels[4], task_labels[9]),
    (task_labels[5], task_labels[9]),
    (task_labels[6], task_labels[10]),
    (task_labels[7], task_labels[10]),
    (task_labels[8], task_labels[11]),
    (task_labels[9], task_labels[12]),
    (task_labels[10], task_labels[12]),
    (task_labels[11], task_labels[12]),
]

# Add nodes and edges to the graph
for task, duration in tasks.items():
    G.add_node(task, duration=duration)

G.add_edges_from(dependencies)

# Calculate earliest start times and latest finish times
earliest_start = {}
latest_finish = {}

# Forward pass
for task in nx.topological_sort(G):
    predecessors = list(G.predecessors(task))
    if not predecessors:
        earliest_start[task] = 0
    else:
        earliest_start[task] = max(
            earliest_start[pred] + G.nodes[pred]["duration"] for pred in predecessors
        )

# Backward pass
for task in reversed(list(nx.topological_sort(G))):
    successors = list(G.successors(task))
    if not successors:
        latest_finish[task] = earliest_start[task] + G.nodes[task]["duration"]
    else:
        latest_finish[task] = min(
            latest_finish[succ] - G.nodes[task]["duration"] for succ in successors
        )

# Identify critical path
critical_path = []
current_task = task_labels[0]  # Start with the first task
while current_task is not None:
    critical_path.append(current_task)
    successors = list(G.successors(current_task))
    if not successors:
        break
    current_task = max(successors, key=lambda x: latest_finish[x])

# Calculate critical path duration
critical_path_duration = sum(G.nodes[task]["duration"] for task in critical_path)

# Print earliest finish time for each task
for task in G.nodes():
    finish_time = earliest_start[task] + G.nodes[task]["duration"]
    print(f"Task {task}: Earliest finish time is {finish_time}")

print(f"Critical Path: {critical_path}")
print(f"Total Duration: {critical_path_duration}")

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(
    G,
    pos,
    with_labels=False,  # We'll add custom labels
    node_color="lightblue",
    node_size=2000,
    font_size=10,
    font_weight="bold",
)

# Add custom labels with task names and durations
labels = {node: f"{node}\n({G.nodes[node]['duration']})" for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels, font_size=8)

# Highlight critical path in red
critical_edges = [
    (critical_path[i], critical_path[i + 1]) for i in range(len(critical_path) - 1)
]
nx.draw_networkx_edges(G, pos, edgelist=critical_edges, edge_color="r", width=2)

plt.show()
