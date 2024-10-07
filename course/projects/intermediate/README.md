### Intermediate-Level Python Exercises

#### **Exercise 1: Working with Modules and APIs**
Use the `requests` library to fetch data from a public API (like JSONPlaceholder or any other free API). Write a function that retrieves a list of items (e.g., posts, users) and processes it by displaying only specific fields (e.g., title or name). Handle possible exceptions, such as network issues or invalid responses.

#### **Exercise 2: Generators and File Processing**
Create a generator function that reads large log files in chunks (e.g., 100 lines at a time). The function should yield these chunks one at a time. Write another function that processes each chunk by searching for specific keywords (e.g., "ERROR"). If an error is found, log it into a separate file. Ensure that file handling is done correctly with `with` statements.

#### **Exercise 3: Classes, Inheritance, and Custom Exceptions**
Define a base class `Employee` with attributes like `name`, `position`, and `salary`. Create two subclasses: `Manager` and `Developer`, each with additional methods specific to their roles. Also, define a custom exception `InvalidSalaryException` that is raised if a negative salary is assigned. Implement salary validation and demonstrate this by creating objects for each class.