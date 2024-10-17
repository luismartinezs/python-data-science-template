from datetime import datetime, timedelta

now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)
future = now + timedelta(days=7)
print(future.strftime("%Y-%m-%d %H:%M:%S"))


import os

# Get the home directory
home_dir = os.path.expanduser("~")

folder_name = "test_folder"

try:
    os.mkdir(folder_name)
    print(f"Folder {folder_name} created")
except FileExistsError:
    print(f"Folder {folder_name} already exists")
finally:
    os.rmdir(folder_name)
    print(f"Folder {folder_name} removed")

import json
from pathlib import Path

try:
    with open(Path(__file__).parent / "data.json", "r") as file:
        data = json.load(file)
        print(f"Name: {data['name']} - Age: {data['age']} - Email: {data['email']}")
except FileNotFoundError:
    print("File not found")
