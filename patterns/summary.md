# Patterns

- List Comprehensions
- Dictionary and Set Comprehensions
- Generators and Generator Expressions
- Context Managers (`with ContextManager() as y:`)
- Decorators
- EAFP (Easier to Ask Forgiveness than Permission)
  - assume necessary conditions and handle exceptions if not
- Unpacking Sequences (`a, b = 5, 10`, `x,y,z = numbers`)
- Using Enumerate and Zip
- Using Collections Module (specialzied datatypes)
- @property Decorator (easy getters and setters)
- Using `any()` and `all()`
- Using `set` for Membership Testing: check if element is in set (cheaper than checking list)
- Data Classes (Python 3.7+): @dataclass, easy create classes mainly for storing data
- Variable Number of Arguments (*args, **kwargs)
- Chaining Comparisons: `1 < x < 10`

# Anti-patterns

- Using mutable objects (list, dicts) as default argument values
  - set default value as None and initialize within function
- Overusing `try-except` Blocks, catching exceptions without specifying the type
  - Always specify exception type
- Ignoring Iterable Tools: using loops instead of built-in functions (max, sum, min, any, all, etc)