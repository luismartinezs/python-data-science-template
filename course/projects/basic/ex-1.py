import os

current_dir = os.path.dirname(os.path.abspath(__file__))

num_lines = 0
try:
    with open(current_dir + "/data.txt", "r") as file:
        for line in file:
            print(line)
            num_lines += 1
except FileNotFoundError:
    print("File not found")

with open(current_dir + "/summary.txt", "w") as file:
    file.write(f"Number of lines: {num_lines}")
