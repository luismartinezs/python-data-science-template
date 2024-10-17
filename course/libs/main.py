"""
Python Standard Library provides a wealth of modules that allow you to perform a wide range of tasks without needing external dependencies. Here, we’ll explore some essential modules that every Python developer should know: datetime, math, random, os, sys, and json
"""

from datetime import datetime

now = datetime.now()
print(now)  # Current date and time

formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)  # e.g., '2024-10-07 10:30:00'

from datetime import timedelta

future_date = now + timedelta(days=10)
print(future_date)  # 10 days from today

import math

print(math.sqrt(16))  # Square root: 4.0
print(math.factorial(5))  # Factorial: 120
print(math.pi)  # Value of Pi: 3.14159...

angle = math.radians(90)  # Convert degrees to radians
print(math.sin(angle))  # Sine of 90 degrees: 1.0

import random

print(random.random())  # Random float between 0 and 1
print(random.randint(1, 10))  # Random integer between 1 and 10

my_list = [1, 2, 3, 4, 5]
print(random.choice(my_list))  # Randomly selects one element

random.shuffle(my_list)
print(my_list)  # List shuffled randomly

import os

current_dir = os.getcwd()  # Get the current directory
print(current_dir)

os.mkdir("new_folder")  # Create a new directory
os.rmdir("new_folder")  # Remove the directory

file_path = os.path.join(current_dir, "example.txt")
print(file_path)  # Combine directory and file into a path

home_dir = os.getenv("HOME")
print(home_dir)  # Prints the user's home directory

"""
The sys module allows you to interact with the Python interpreter. It provides functions to manipulate the Python runtime environment and command-line arguments
"""

import sys

print(sys.argv)  # List of command-line arguments passed to the script

# sys.exit(0)  # Exits the program with a status code of 0 (success)

print(sys.version)  # Prints the Python version being used


import json

json_data = '{"name": "Luis", "age": 30}'
data = json.loads(json_data)  # Convert JSON string to Python dict
print(data["name"])  # Output: Luis

person = {"name": "Luis", "age": 30}
json_string = json.dumps(person)
print(json_string)  # Output: '{"name": "Luis", "age": 30}'

from pathlib import Path

with open(Path(__file__).parent / "data.json", "r") as file:
    data = json.load(file)  # Load JSON from a file
    print(data)
