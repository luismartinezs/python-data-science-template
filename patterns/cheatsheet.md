# Python Patterns and Anti-Patterns Cheatsheet

Quick reference guide to common Python coding patterns and anti-patterns.

---

## **1. List Comprehensions**

Create lists in a concise way.

**Pattern:**

```python
squares = [x**2 for x in range(1, 11)]
```

**Output:**

```python
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

---

## **2. Dictionary and Set Comprehensions**

Create dictionaries and sets using comprehensions.

**Dictionary Comprehension:**

```python
cubes = {x: x**3 for x in range(1, 6)}
```

**Set Comprehension:**

```python
first_letters = {word[0] for word in words}
```

---

## **3. Generators and Generator Expressions**

Iterate over sequences without storing them in memory.

**Generator Function:**

```python
def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b
```

**Generator Expression:**

```python
squares = (x**2 for x in range(1, 11))
```

---

## **4. Context Managers**

Manage resources with the `with` statement.

**Using `with` for Files:**

```python
with open('example.txt', 'r') as file:
    content = file.read()
```

**Custom Context Manager:**

```python
from contextlib import contextmanager

@contextmanager
def timer():
    start_time = time.time()
    yield
    print(f"Elapsed time: {time.time() - start_time} seconds")
```

---

## **5. Decorators**

Modify or enhance functions.

**Function Decorator:**

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def greet(name):
    print(f"Hello, {name}!")
```

---

## **6. EAFP (Easier to Ask Forgiveness than Permission)**

Assume valid conditions and handle exceptions if not.

**Example:**

```python
try:
    age = data['age']
except KeyError:
    age = 'Unknown'
```

---

## **7. Unpacking Sequences**

Assign elements to variables in one statement.

**Example:**

```python
a, b = b, a

name, age, position = employee
```

---

## **8. Using `enumerate()` and `zip()`**

Add counters or combine iterables.

**Enumerate:**

```python
for index, value in enumerate(['a', 'b', 'c']):
    print(index, value)
```

**Zip:**

```python
for name, score in zip(names, scores):
    print(f"{name} scored {score}")
```

---

## **9. Using `collections` Module**

Specialized container datatypes.

**Counter:**

```python
from collections import Counter
count = Counter(words)
```

**Defaultdict:**

```python
from collections import defaultdict
groups = defaultdict(list)
for word in words:
    groups[word[0]].append(word)
```

---

## **10. `@property` Decorator**

Use getters and setters elegantly.

**Example:**

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius cannot be negative")
```

---

## **11. Using `any()` and `all()`**

Check boolean conditions in iterables.

**Any:**

```python
has_even = any(n % 2 == 0 for n in numbers)
```

**All:**

```python
all_valid = all(len(pwd) >= min_length for pwd in passwords)
```

---

## **12. Using `set` for Membership Testing**

Efficient membership checks.

**Example:**

```python
if user_input in valid_entries:
    print("Valid entry")
```

---

## **13. Data Classes (Python 3.7+)**

Simplify class definitions.

**Example:**

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
```

---

## **14. Variable Number of Arguments**

Accept arbitrary arguments.

**Using `*args`:**

```python
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result
```

---

## **15. Chaining Comparisons**

Concise conditional expressions.

**Example:**

```python
if 18 <= age <= 65:
    print("Valid age")
```

---

## **Anti-Patterns to Avoid**

### **1. Mutable Default Arguments**

**Anti-Pattern:**

```python
def func(val, my_list=[]):
    my_list.append(val)
    return my_list
```

**Issue:** Default list persists between calls.

**Proper Pattern:**

```python
def func(val, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(val)
    return my_list
```

---

### **2. Overusing `try-except` Blocks**

**Anti-Pattern:**

```python
try:
    risky_code()
except:
    handle_error()
```

**Issue:** Catches all exceptions, including unexpected ones.

**Proper Pattern:**

```python
try:
    risky_code()
except SpecificException:
    handle_error()
```

---

### **3. Ignoring Iterable Tools**

**Anti-Pattern:**

```python
total = 0
for num in numbers:
    total += num
```

**Proper Pattern:**

```python
total = sum(numbers)
```

---

## **Tips**

- Use list/dictionary/set comprehensions for concise and readable code.
- Utilize generators for memory efficiency with large datasets.
- Employ context managers for resource management.
- Embrace EAFP over LBYL (Look Before You Leap).
- Leverage built-in functions and modules (`enumerate()`, `zip()`, `collections`, `any()`, `all()`, etc.).
- Avoid common anti-patterns to prevent bugs and improve code quality.

---

**Remember:** Writing Pythonic code enhances readability and maintainability. Keep practicing these patterns to internalize them.