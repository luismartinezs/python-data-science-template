# Common Python Code Patterns

Learning common code patterns is crucial for writing clean, efficient, and "Pythonic" code. These patterns help you solve problems effectively and make your code more readable and maintainable. This guide introduces you to widely used Python coding patterns, along with examples and exercises to practice. We'll also highlight some anti-patterns to avoid common pitfalls.

Let's dive in!

---

## **1. List Comprehensions**

### **Introduction**

List comprehensions provide a concise way to create lists based on existing iterables. They are more readable and often faster than using loops to create lists.

### **Example**

Create a list of squares for numbers from 1 to 10:

```python
squares = [x**2 for x in range(1, 11)]
print(squares)
```

**Output:**

```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

### **Exercise**

Given a list of integers, create a new list that contains only the even numbers from the original list using a list comprehension.

**Starter Code:**

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Your code here
```

---

## **2. Dictionary and Set Comprehensions**

### **Introduction**

Similar to list comprehensions, but for dictionaries and sets.

### **Example**

Create a dictionary where keys are numbers from 1 to 5 and values are their cubes:

```python
cubes = {x: x**3 for x in range(1, 6)}
print(cubes)
```

**Output:**

```
{1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
```

### **Exercise**

Given a list of words, create a set of unique first letters using a set comprehension.

**Starter Code:**

```python
words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
# Your code here
```

---

## **3. Generators and Generator Expressions**

### **Introduction**

Generators allow you to iterate over sequences without storing the entire sequence in memory. They generate values on the fly using the `yield` statement.

### **Example**

Create a generator that yields Fibonacci numbers up to `n`:

```python
def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)
```

**Output:**

```
0
1
1
2
3
5
8
```

### **Exercise**

Write a generator expression that generates the squares of numbers from 1 to 10 without using a list comprehension.

**Starter Code:**

```python
squares = # Your code here
for num in squares:
    print(num)
```

---

## **4. Context Managers**

### **Introduction**

Context managers allow you to allocate and release resources precisely when you want to. The most common use is with the `with` statement in file operations.

### **Example**

Open a file, read its content, and ensure it's properly closed after:

```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# File is automatically closed here.
```

### **Exercise**

Create a custom context manager using the `contextlib` module that measures the execution time of a code block.

**Starter Code:**

```python
import time
from contextlib import contextmanager

@contextmanager
def timer():
    # Your code here
    pass

with timer():
    # Some code whose execution time you want to measure
    total = sum(range(1000000))
```

---

## **5. Decorators**

### **Introduction**

Decorators are a powerful pattern that allows you to modify the behavior of a function or class. They are often used for logging, enforcing access control, instrumentation, and caching.

### **Example**

Create a decorator that logs the function name every time it's called:

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Executing function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

**Output:**

```
Executing function: greet
Hello, Alice!
```

### **Exercise**

Write a decorator named `timer` that measures and prints the execution time of the decorated function.

**Starter Code:**

```python
import time

def timer(func):
    # Your code here
    pass

@timer
def compute():
    total = sum(range(1000000))
    return total

compute()
```

---

## **6. EAFP (Easier to Ask Forgiveness than Permission)**

### **Introduction**

Python encourages the EAFP coding style, where you assume the necessary conditions are met and handle exceptions if they are not.

### **Example**

Access an element in a dictionary:

```python
data = {'name': 'Alice', 'age': 25}

# EAFP style
try:
    age = data['age']
except KeyError:
    age = 'Unknown'

print(age)
```

### **Exercise**

Given a list of files, attempt to open each one and handle the `FileNotFoundError` if a file does not exist.

**Starter Code:**

```python
filenames = ['file1.txt', 'file2.txt', 'file3.txt']
for filename in filenames:
    # Your code here
    pass
```

---

## **7. Unpacking Sequences**

### **Introduction**

Unpacking allows you to assign elements of a sequence to multiple variables in a single statement.

### **Example**

Swap two variables:

```python
a, b = 5, 10
a, b = b, a
print(a, b)  # Output: 10 5
```

### **Exercise**

Given a tuple containing employee data (`name`, `age`, `position`), unpack the values into separate variables.

**Starter Code:**

```python
employee = ('John Doe', 30, 'Software Engineer')
# Your code here
```

---

## **8. Using Enumerate and Zip**

### **Introduction**

- `enumerate()` adds a counter to an iterable.
- `zip()` combines multiple iterables into an iterator of tuples.

### **Example**

Using `enumerate`:

```python
for index, value in enumerate(['a', 'b', 'c']):
    print(index, value)
```

**Output:**

```
0 a
1 b
2 c
```

Using `zip`:

```python
questions = ['name', 'quest', 'favorite color']
answers = ['Lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print(f"What is your {q}? It is {a}.")
```

### **Exercise**

Write a program that takes two lists, `names` and `scores`, and prints each name with the corresponding score using `zip`.

**Starter Code:**

```python
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]
# Your code here
```

---

## **9. Using Collections Module**

### **Introduction**

The `collections` module provides specialized container data types like `defaultdict`, `Counter`, and `namedtuple`.

### **Example**

Using `Counter` to count occurrences:

```python
from collections import Counter

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
count = Counter(words)
print(count)
```

**Output:**

```
Counter({'apple': 3, 'banana': 2, 'orange': 1})
```

### **Exercise**

Use `defaultdict` to group a list of words by their first letters.

**Starter Code:**

```python
from collections import defaultdict

words = ['apple', 'apricot', 'banana', 'blueberry', 'cherry', 'cranberry']
groups = defaultdict(list)
# Your code here
```

---

## **10. @property Decorator**

### **Introduction**

Pythonic way to use getters and setters without explicitly defining methods. The `@property` decorator allows you to define methods that can be accessed like attributes.

### **Example**

Using `@property`:

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        print("Getting radius")
        return self._radius

    @radius.setter
    def radius(self, value):
        print("Setting radius")
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius cannot be negative")

c = Circle(5)
print(c.radius)  # Getting radius
c.radius = 10    # Setting radius
```

### **Exercise**

Refactor the following class to use `@property` instead of explicit getter and setter methods:

```python
class Employee:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

emp = Employee('John')
print(emp.get_name())
emp.set_name('Jane')
print(emp.get_name())
```

---

## **11. Using `any()` and `all()`**

### **Introduction**

- `any()` returns `True` if any element in the iterable is `True`.
- `all()` returns `True` if all elements in the iterable are `True`.

### **Example**

Check if any number in a list is even:

```python
numbers = [1, 3, 5, 7, 2]
has_even = any(n % 2 == 0 for n in numbers)
print(has_even)  # Output: True
```

### **Exercise**

Given a list of passwords, check if all passwords meet the minimum length requirement using `all()`.

**Starter Code:**

```python
passwords = ['abcdef', '12345678', 'pass', 'wordpass']
min_length = 6
# Your code here
```

---

## **12. Using `set` for Membership Testing**

### **Introduction**

Sets offer O(1) time complexity for membership tests, making them more efficient than lists for large datasets.

### **Example**

Check if items exist in a collection:

```python
valid_entries = {'apple', 'banana', 'cherry'}
user_input = 'banana'

if user_input in valid_entries:
    print("Valid entry")
else:
    print("Invalid entry")
```

### **Exercise**

Given a list of email addresses, check which ones are in a set of known spam emails.

**Starter Code:**

```python
spam_emails = {'spam@example.com', 'junk@mail.com', 'fake@domain.com'}
emails = ['user1@example.com', 'spam@example.com', 'user2@mail.com', 'fake@domain.com']
# Your code here
```

---

## **13. Data Classes (Python 3.7+)**

### **Introduction**

Data classes reduce boilerplate code when creating classes that primarily store data.

### **Example**

Using `@dataclass`:

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(10, 20)
print(p)
```

**Output:**

```
Point(x=10, y=20)
```

### **Exercise**

Create a data class `Book` with attributes `title`, `author`, and `year`, and instantiate it with sample data.

**Starter Code:**

```python
from dataclasses import dataclass

# Your code here
```

---

## **14. Variable Number of Arguments**

### **Introduction**

Functions can accept arbitrary numbers of positional and keyword arguments using `*args` and `**kwargs`.

### **Example**

Function that accepts any number of positional arguments:

```python
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply(2, 3, 4))  # Output: 24
```

### **Exercise**

Write a function `greet_all` that accepts any number of names and prints a greeting for each.

**Starter Code:**

```python
def greet_all(*names):
    # Your code here
    pass

greet_all('Alice', 'Bob', 'Charlie')
```

---

## **15. Chaining Comparisons**

### **Introduction**

Python allows you to chain comparison operators for more concise expressions.

### **Example**

Check if a number is between 1 and 10:

```python
x = 5
if 1 < x < 10:
    print("x is between 1 and 10")
```

### **Exercise**

Write a function `is_valid_age` that returns `True` if the age is between 18 and 65 inclusive.

**Starter Code:**

```python
def is_valid_age(age):
    # Your code here
    pass

print(is_valid_age(20))  # Should be True
print(is_valid_age(70))  # Should be False
```

---

## **Anti-Patterns to Avoid**

### **1. Mutable Default Arguments**

**Anti-Pattern:**

Using mutable objects (like lists or dictionaries) as default argument values can lead to unexpected behavior.

```python
def append_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list

print(append_to_list(1))  # Output: [1]
print(append_to_list(2))  # Output: [1, 2] - unexpected!
```

**Proper Pattern:**

Use `None` as the default value and assign a new mutable object inside the function.

```python
def append_to_list(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list

print(append_to_list(1))  # Output: [1]
print(append_to_list(2))  # Output: [2]
```

### **Exercise**

Identify and fix the issue in the following function:

```python
def add_employee(name, employees={}):
    employees[name] = True
    return employees

team_a = add_employee('Alice')
team_b = add_employee('Bob')

print(team_a)
print(team_b)
```

---

### **2. Overusing `try-except` Blocks**

**Anti-Pattern:**

Catching exceptions without specifying the exception type can mask other errors.

```python
try:
    # Code that may raise an exception
except:
    # Handle the error
```

**Proper Pattern:**

Specify the exception type.

```python
try:
    result = 10 / divisor
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

### **Exercise**

Review the following code and modify it to catch only the appropriate exceptions:

```python
try:
    index = int(input("Enter an index: "))
    print(my_list[index])
except:
    print("An error occurred.")
```

---

### **3. Ignoring Iterable Tools**

**Anti-Pattern:**

Using loops where built-in functions like `sum`, `max`, `min`, or comprehensions would be more efficient.

```python
total = 0
for num in numbers:
    total += num
```

**Proper Pattern:**

Use built-in functions.

```python
total = sum(numbers)
```

### **Exercise**

Refactor the following code to use a built-in function:

```python
found = False
for num in numbers:
    if num > 100:
        found = True
        break
```

---

## **Conclusion**

Understanding and applying these common Python code patterns will greatly enhance your coding skills. Practice these patterns through the exercises provided, and try to recognize and avoid anti-patterns in your code.

Remember, writing "Pythonic" code isn't just about making your code run—it’s about making it elegant, readable, and maintainable. Happy coding!

---

## **Solutions to Exercises**

### **Exercise 1 Solution**

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)
```

### **Exercise 2 Solution**

```python
words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
first_letters = {word[0] for word in words}
print(first_letters)
```

### **Exercise 3 Solution**

```python
squares = (x**2 for x in range(1, 11))
for num in squares:
    print(num)
```

### **Exercise 4 Solution**

```python
import time
from contextlib import contextmanager

@contextmanager
def timer():
    start_time = time.time()
    yield
    end_time = time.time()
    print(f"Elapsed time: {end_time - start_time} seconds")

with timer():
    total = sum(range(1000000))
```

### **Exercise 5 Solution**

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds")
        return result
    return wrapper

@timer
def compute():
    total = sum(range(1000000))
    return total

compute()
```

### **Exercise 6 Solution**

```python
filenames = ['file1.txt', 'file2.txt', 'file3.txt']
for filename in filenames:
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Contents of {filename}:")
            print(content)
    except FileNotFoundError:
        print(f"{filename} not found.")
```

### **Exercise 7 Solution**

```python
employee = ('John Doe', 30, 'Software Engineer')
name, age, position = employee
print(name)
print(age)
print(position)
```

### **Exercise 8 Solution**

```python
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")
```

### **Exercise 9 Solution**

```python
from collections import defaultdict

words = ['apple', 'apricot', 'banana', 'blueberry', 'cherry', 'cranberry']
groups = defaultdict(list)
for word in words:
    groups[word[0]].append(word)

print(dict(groups))
```

### **Exercise 10 Solution**

```python
class Employee:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

emp = Employee('John')
print(emp.name)
emp.name = 'Jane'
print(emp.name)
```

### **Exercise 11 Solution**

```python
passwords = ['abcdef', '12345678', 'pass', 'wordpass']
min_length = 6
all_valid = all(len(pwd) >= min_length for pwd in passwords)
print(all_valid)
```

### **Exercise 12 Solution**

```python
spam_emails = {'spam@example.com', 'junk@mail.com', 'fake@domain.com'}
emails = ['user1@example.com', 'spam@example.com', 'user2@mail.com', 'fake@domain.com']

for email in emails:
    if email in spam_emails:
        print(f"{email} is spam.")
    else:
        print(f"{email} is valid.")
```

### **Exercise 13 Solution**

```python
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    year: int

book = Book('1984', 'George Orwell', 1949)
print(book)
```

### **Exercise 14 Solution**

```python
def greet_all(*names):
    for name in names:
        print(f"Hello, {name}!")

greet_all('Alice', 'Bob', 'Charlie')
```

### **Exercise 15 Solution**

```python
def is_valid_age(age):
    return 18 <= age <= 65

print(is_valid_age(20))  # True
print(is_valid_age(70))  # False
```

### **Anti-Pattern Exercise Solutions**

#### **Mutable Default Arguments Exercise Solution**

```python
def add_employee(name, employees=None):
    if employees is None:
        employees = {}
    employees[name] = True
    return employees

team_a = add_employee('Alice')
team_b = add_employee('Bob')

print(team_a)  # {'Alice': True}
print(team_b)  # {'Bob': True}
```

#### **Overusing `try-except` Blocks Exercise Solution**

```python
try:
    index = int(input("Enter an index: "))
    print(my_list[index])
except ValueError:
    print("Please enter a valid integer.")
except IndexError:
    print("Index is out of range.")
```

#### **Ignoring Iterable Tools Exercise Solution**

```python
found = any(num > 100 for num in numbers)
```

---

**Note:** Practice these patterns regularly, and soon they will become a natural part of your coding style. Keep exploring and experimenting with different approaches to find the most effective solutions.