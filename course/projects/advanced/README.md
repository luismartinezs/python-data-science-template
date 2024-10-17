### Advanced-Level Python Exercises

#### **Exercise 1: Decorators and Logging**
Write a decorator `time_logger` that logs the execution time of any function it decorates. Use the `time` module to calculate the time difference. Apply this decorator to a function that performs a complex calculation (e.g., finding the nth Fibonacci number using recursion). Additionally, log the start and end time of the function execution.

#### **Exercise 2: Advanced Class Design and Context Managers**
Create a class `DatabaseConnection` that mimics opening and closing a database connection. Implement it as a context manager using the `__enter__` and `__exit__` methods. Simulate connecting to and disconnecting from a database (you can print messages for simulation). Ensure that even if an exception occurs during the connection, the database is properly closed. Test this with a function that performs multiple queries and throws an exception.

#### **Exercise 3: Iterators and Generators with Custom Exceptions**
Create an iterator class `EvenNumbers` that iterates through even numbers within a specified range. The class should raise a custom exception `OutOfRangeException` if an attempt is made to access a number outside the defined range. Additionally, implement a generator that does the same but in a more memory-efficient way.