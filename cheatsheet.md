# Python Cheatsheet

This cheatsheet provides a quick reference to the essentials of Python programming. It covers fundamental concepts, syntax, and commonly used libraries to help you write Python code efficiently.

---

## **Basic Syntax**

### **Comments**

```python
# Single-line comment

"""
Multi-line comment or docstring
"""

'''
Another way to write multi-line comments
'''
```

### **Variables and Data Types**

- Variables are dynamically typed; you don't need to declare the type.

```python
x = 10          # Integer
y = 3.14        # Float
name = "Alice"  # String
is_valid = True # Boolean
```

### **Printing Output**

```python
print("Hello, World!")
print(f"Name: {name}, Age: {x}")
```

### **User Input**

```python
user_input = input("Enter something: ")
```

---

## **Control Flow Statements**

### **Conditional Statements**

```python
if condition:
    # Code block
elif another_condition:
    # Another code block
else:
    # Else code block
```

**Example:**

```python
age = 18
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

### **Loops**

#### **For Loops**

```python
for item in iterable:
    # Code block
```

**Example:**

```python
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
```

#### **Range Function**

```python
for i in range(5):        # 0 to 4
for i in range(1, 5):     # 1 to 4
for i in range(0, 10, 2): # 0 to 8, step of 2
```

#### **While Loops**

```python
while condition:
    # Code block
```

**Example:**

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

#### **Loop Control Statements**

```python
break    # Exit the loop
continue # Skip to the next iteration
pass     # Do nothing
```

---

## **List Comprehension**

Compact way to create lists.

```python
new_list = [expression for item in iterable if condition]
```

**Examples:**

```python
squares = [x**2 for x in range(1, 11)]
even_numbers = [x for x in range(20) if x % 2 == 0]
```

---

## **Data Structures**

### **Lists**

- Mutable, ordered sequence of items.

```python
my_list = [1, 2, 3, 'a', 'b', 'c']
my_list.append(4)
my_list.extend([5, 6])
my_list.insert(0, 'start')
item = my_list.pop()     # Removes last item
my_list.remove('a')      # Removes first occurrence
```

### **Tuples**

- Immutable, ordered sequence of items.

```python
my_tuple = (1, 2, 3)
single_item_tuple = (1,)
```

### **Sets**

- Unordered collection of unique items.

```python
my_set = {1, 2, 3, 2}
my_set.add(4)
my_set.update([5, 6])
my_set.remove(2)
```

### **Dictionaries**

- Key-value pairs, unordered.

```python
my_dict = {'name': 'Alice', 'age': 25}
my_dict['email'] = 'alice@example.com'
value = my_dict.get('age')
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()
```

---

## **Functions**

### **Defining Functions**

```python
def function_name(parameters):
    # Code block
    return value
```

**Example:**

```python
def add(a, b):
    return a + b
```

### **Default Arguments**

```python
def greet(name='Guest'):
    print(f"Hello, {name}!")
```

### **Variable-Length Arguments**

```python
def func(*args, **kwargs):
    # args is a tuple of positional arguments
    # kwargs is a dictionary of keyword arguments
```

**Example:**

```python
def multiply(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result
```

### **Lambda Functions**

Anonymous, small functions.

```python
lambda_arguments: expression

square = lambda x: x**2
print(square(5))  # Output: 25
```

---

## **Modules and Packages**

### **Importing Modules**

```python
import module_name
import module_name as alias
from module_name import function_name
from module_name import function1, function2
from module_name import *  # Import all (not recommended)
```

**Example:**

```python
import math
from math import sqrt, pi
```

### **Creating Modules**

- Save your functions in a `.py` file and import it.

**my_module.py:**

```python
def my_function():
    print("Hello from my_module")
```

**main.py:**

```python
import my_module
my_module.my_function()
```

### **Packages**

- Directories containing an `__init__.py` file.

**Directory structure:**

```
my_package/
    __init__.py
    module1.py
    module2.py
```

**Usage:**

```python
from my_package import module1
```

### **Using `pip` for Package Management**

- Install packages from the Python Package Index (PyPI).

```bash
pip install package_name
pip uninstall package_name
pip list
pip install -r requirements.txt  # Install from file
```

---

## **Classes and Objects**

### **Defining a Class**

```python
class ClassName:
    class_variable = 'Shared value'  # Class variable

    def __init__(self, parameter1, parameter2):
        self.instance_variable1 = parameter1
        self.instance_variable2 = parameter2

    def instance_method(self):
        # Code block
        pass

    @classmethod
    def class_method(cls):
        # Code block
        pass

    @staticmethod
    def static_method():
        # Code block
        pass
```

### **Creating Objects**

```python
obj = ClassName(arg1, arg2)
```

### `@classmethod` Example: Alternative Constructor

```python
class Car:
	default_setups = {
		'sedan': {'seats': 5, 'doors': 4, 'fuel': 'petrol'},
		'suv': {'seats': 7, 'doors': 5, 'fuel': 'diesel'}
	}

	def __init__(self, seats, doors, fuel):
		self.seats = seats
		self.doors = doors
		self.fuel = fuel

	@classmethod
	def from_model(cls, model):
		setup = cls.default_setups.get(model)
		if not setup:
			raise ValueError(f"No setup for '{model}'")
		return cls(**setup)
```

**Usage:** `car = Car.from_model('suv')`

---

### `@staticmethod` Example: Utility Function

```python
class BankAccount:
	@staticmethod
	def calculate_interest(amount, rate):
		return amount * rate / 100
```

**Usage:** `interest = BankAccount.calculate_interest(1000, 5)`


### **Inheritance**

```python
class ChildClass(ParentClass):
    def __init__(self, args):
        super().__init__(args)
        # Additional initialization
```

### **Method Overriding**

- Redefine methods in the child class.

### **Special Methods**

- Also known as "magic methods" or "dunder methods".

```python
def __str__(self):
    return "String representation"

def __repr__(self):
    return "Official representation"
```

---

## **Exception Handling**

### **Try-Except Block**

```python
try:
    # Code that may raise an exception
except ExceptionType:
    # Code to handle the exception
else:
    # Code to execute if no exception occurred
finally:
    # Code to execute regardless of exceptions
```

**Example:**

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
finally:
    print("Execution complete.")
```

### **Raising Exceptions**

```python
raise ExceptionType("Error message")
```

**Example:**

```python
if age < 0:
    raise ValueError("Age cannot be negative")
```

### **Custom Exceptions**

```python
class CustomError(Exception):
    pass

raise CustomError("Custom error occurred")
```

---

## **File I/O**

### **Opening Files**

```python
file = open('filename.txt', 'mode')
```

**Modes:**

- `'r'` - Read (default)
- `'w'` - Write (truncate)
- `'a'` - Append
- `'rb'`, `'wb'` - Binary modes

### **Reading Files**

```python
file = open('file.txt', 'r')
content = file.read()
lines = file.readlines()
file.close()
```

### **Writing Files**

```python
file = open('file.txt', 'w')
file.write("Hello, World!")
file.close()
```

### **Using Context Managers**

- Automatically handles file closing.

```python
with open('file.txt', 'r') as file:
    content = file.read()
```

---

## **Standard Libraries**

### **Math Operations**

```python
import math

math.pi
math.sqrt(16)
math.factorial(5)
```

### **Random Numbers**

```python
import random

random.random()          # Random float between 0.0 to 1.0
random.randint(1, 10)    # Random integer between 1 and 10
random.choice(sequence)  # Random element from a sequence
```

### **Date and Time**

```python
import datetime

now = datetime.datetime.now()
today = datetime.date.today()
delta = datetime.timedelta(days=10)
```

### **OS Module**

```python
import os

os.getcwd()            # Get current working directory
os.listdir()           # List files in directory
os.mkdir('new_dir')    # Create new directory
os.remove('file.txt')  # Remove file
```

### **Sys Module**

```python
import sys

sys.argv          # Command-line arguments
sys.path          # Python module search path
sys.version       # Python version
```

### **JSON Module**

```python
import json

data = {'name': 'Alice', 'age': 25}
json_str = json.dumps(data)
data_dict = json.loads(json_str)

# Working with files
with open('data.json', 'w') as f:
    json.dump(data, f)

with open('data.json', 'r') as f:
    data = json.load(f)
```

---

## **Third-Party Libraries**

### **Installing Packages with `pip`**

```bash
pip install requests
```

### **Using the `requests` Library**

```python
import requests

response = requests.get('https://api.example.com/data')
if response.status_code == 200:
    data = response.json()
```

**Basic Usage:**

```python
# GET request
response = requests.get('https://api.example.com/data')

# POST request
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://api.example.com/data', data=payload)

# Handling response
print(response.status_code)
print(response.text)
```

---

## **Iterators, Generators, and Decorators**

### **Iterators**

An object that can be iterated upon.

```python
iterable = [1, 2, 3]
iterator = iter(iterable)
print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
```

### **Generators**

Functions that yield sequence of values using the `yield` keyword.

```python
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
```

**Example:**

```python
def fib(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

for number in fib(10):
    print(number)
```

### **Decorators**

Functions that modify the behavior of other functions.

```python
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        # Code before
        result = original_function(*args, **kwargs)
        # Code after
        return result
    return wrapper_function
```

**Using Decorators:**

```python
@decorator_function
def display():
    print("Display function ran")

display()
```

**Example: Logging Decorator:**

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Running function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(x, y):
    return x + y

print(add(5, 3))
```

---

## **Additional Important Topics**

### **List, Dictionary, and Set Comprehensions**

- **List Comprehension:**

  ```python
  squares = [x**2 for x in range(10)]
  even_squares = [x**2 for x in range(10) if x % 2 == 0]
  ```

- **Dictionary Comprehension:**

  ```python
  dict_comp = {x: x**2 for x in range(5)}
  ```

- **Set Comprehension:**

  ```python
  set_comp = {x for x in 'hello' if x not in 'aeiou'}
  ```

### **Working with Strings**

```python
s = "Hello, World!"

s.upper()
s.lower()
s.strip()
s.replace('Hello', 'Hi')
s.split(',')
```

### **Regular Expressions**

```python
import re

pattern = r'\d+'
text = 'There are 42 apples'

matches = re.findall(pattern, text)
match = re.search(pattern, text)
```

### **Assertions**

```python
assert condition, "Error message if condition is False"
```

**Example:**

```python
def divide(a, b):
    assert b != 0, "Denominator cannot be zero"
    return a / b
```

### **Type Hints (PEP 484)**

```python
def greeting(name: str) -> str:
    return 'Hello ' + name
```

**Type Hinting with Variables:**

```python
age: int = 25
names: list[str] = ['Alice', 'Bob']
```

### **Context Managers**

- Use the `with` statement to ensure resources are properly managed.

```python
with open('file.txt', 'w') as file:
    file.write('Hello, World!')
```

- Custom context managers using `__enter__` and `__exit__`:

```python
class MyContextManager:
    def __enter__(self):
        # Setup code
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Teardown code

with MyContextManager() as manager:
    # Code block
```

### **Enumerate and Zip**

- **Enumerate:**

  ```python
  for index, value in enumerate(iterable):
      print(index, value)
  ```

- **Zip:**

  ```python
  for item1, item2 in zip(list1, list2):
      print(item1, item2)
  ```

- **Enumerate** – Iterate with index:
  ```python
  fruits = ['apple', 'banana', 'cherry']

  for index, value in enumerate(fruits):
      print(index, value)

  # Output:
  # 0 apple
  # 1 banana
  # 2 cherry
  ```

- **Zip** – Iterate over multiple iterables in parallel:
  ```python
  names = ['Alice', 'Bob', 'Charlie']
  scores = [85, 92, 78]

  for name, score in zip(names, scores):
      print(name, score)

  # Output:
  # Alice 85
  # Bob 92
  # Charlie 78
  ```

- **Enumerate with Zip** – Indexed iteration over zipped lists:
  ```python
  colors = ['red', 'green', 'blue']
  codes = ['R', 'G', 'B']

  for index, (color, code) in enumerate(zip(colors, codes)):
      print(index, color, code)

  # Output:
  # 0 red R
  # 1 green G
  # 2 blue B
  ```
  ```

### **Unpacking**

```python
a, b = 1, 2
a, *rest = [1, 2, 3, 4]  # a=1, rest=[2, 3, 4]
```

### **Map, Filter, Reduce**

- **Map:**

  ```python
  numbers = [1, 2, 3]
  squares = list(map(lambda x: x**2, numbers))
  ```

- **Filter:**

  ```python
  numbers = [1, 2, 3, 4, 5]
  even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
  ```

- **Reduce:**

  ```python
  from functools import reduce

  total = reduce(lambda x, y: x + y, numbers)
  ```

### **Collections Module**

```python
from collections import Counter, defaultdict, namedtuple

# Counter
counts = Counter('abracadabra')

# defaultdict
dd = defaultdict(list)
dd['key'].append(1)

# namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
```

### **Working with Datetimes**

```python
from datetime import datetime, timedelta

now = datetime.now()
yesterday = now - timedelta(days=1)
formatted_date = now.strftime('%Y-%m-%d')
parsed_date = datetime.strptime('2023-01-01', '%Y-%m-%d')
```

### **Command-Line Arguments**

```python
import sys

args = sys.argv[1:]  # Exclude the script name
```

### **Logging**

```python
import logging

logging.basicConfig(level=logging.INFO)
logging.info('Informational message')
logging.error('An error occurred')
```

### **Copying Objects**

- **Shallow Copy:**

  ```python
  import copy

  list_copy = original_list.copy()
  list_copy = list(original_list)
  ```

- **Deep Copy:**

  ```python
  deep_copy = copy.deepcopy(original_object)
  ```

### **Global and Nonlocal Keywords**

- **Global:**

  ```python
  x = 5

  def update_global():
      global x
      x = 10
  ```

- **Nonlocal:**

  ```python
  def outer():
      x = 'outer'

      def inner():
          nonlocal x
          x = 'inner'

      inner()
      print(x)  # 'inner'
  ```

---

## **Conclusion**

This cheatsheet covers fundamental concepts and common patterns in Python programming. It's a handy reference for quickly recalling syntax and standard practices. Remember, the best way to learn programming is by writing code and building projects. Happy coding!

---

**Note:** This cheatsheet provides concise explanations and examples. For more detailed information, refer to the [official Python documentation](https://docs.python.org/3/).