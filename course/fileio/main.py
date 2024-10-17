"""
file = open('filename', 'mode')
# Perform file operations
file.close()

filename: The name (or path) of the file you want to work with.
mode: This specifies what you want to do with the file. Common modes include:
'r': Read (default mode).
'w': Write (overwrites the file if it exists).
'a': Append (adds to the end of the file without overwriting).
'b': Binary mode (used for non-text files).
'r+': Read and write.
"""

# OPEN
try:
    file = open("example.txt", "r")
    # Do something with the file
except FileNotFoundError:
    print("File not found")
else:
    file.close()

try:
    with open("example.txt", "r") as file:
        data = file.read()
        # No need to manually close the file
except FileNotFoundError:
    print("File not found")

# READ
"""
file.read(): Reads the entire file as a single string.
file.readline(): Reads one line at a time.
file.readlines(): Reads all lines and returns a list of strings.
"""
try:
    with open("example.txt", "r") as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found")

try:
    with open("example.txt", "r") as file:
        for line in file:
            print(line.strip())  # strip() removes the newline characters
except FileNotFoundError:
    print("File not found")

# filepaths
# Using os Module
import os

# Get current directory
current_dir = os.getcwd()

# Join paths safely
full_path = os.path.join(current_dir, "example.txt")
print(full_path)

# Using pathlib (Preferred in Modern Python)
from pathlib import Path

# Define a path
current_dir = Path(__file__).parent
file_name = "example.txt"
file_path = Path(current_dir, file_name)

# Check if a file exists
if file_path.exists():
    print(f"The file {file_path} exists.")
else:
    print(f"The file {file_path} does not exist.")

try:
    with open(file_path, "a") as file:
        file.write("\nHello World 2")
except FileNotFoundError:
    print("File not found")

"""
Best Practices for File I/O

Always close files: Use with open() as it ensures files are closed automatically, even if an exception occurs.

Handle errors: When dealing with file paths or content, it's a good idea to handle errors using try-except.

Work with relative paths: Use relative paths (instead of hardcoding absolute paths) for portability across different systems.
"""

"""
Write a Python program to open and read a file named data.txt, and print each line in the file to the console. Ensure you handle the case where the file does not exist
"""

try:
    with open("data.txt", "r") as file:
        for line in file:
            print(line)
except FileNotFoundError:
    print("File not found")


"""
Write a program that asks the user for their name and age, and writes this information to a file called user_info.txt
"""

name = input("enter your name:")
age = input("enter your age:")

try:
    with open(Path(__file__).parent / "user_info.txt", "w") as file:
        file.write(f"Name: {name}\nAge: {age}")
except FileNotFoundError:
    print("File not found")
