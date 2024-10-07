from math import prod


def greet(name):
    return f"Hello, {name}!"


# Function Invocation
message = greet("Luis")
print(message)  # Output: Hello, Luis!


# positional arguments
def multiply(x, y):
    return x * y


result = multiply(3, 4)  # Output: 12


# keyword arguments
def introduce(name, age):
    return f"{name} is {age} years old."


introduction = introduce(name="Luis", age=28)
print(introduction)  # Output: Luis is 28 years old.


# default arguments
def greet(name="world"):
    return f"Hello, {name}!"


print(greet())  # Output: Hello, world!
print(greet("Luis"))  # Output: Hello, Luis!


# arbitrary positional arguments
def add_all(*args):
    return sum(args)


print(add_all(1, 2, 3, 4))  # Output: 10


# arbitrary keyword arguments
def details(**kwargs):
    return kwargs


print(details(name="Luis", age=28))  # Output: {'name': 'Luis', 'age': 28}

# print(details("luis", 26)) # error

"""
lambda fncs
lambda arguments: expression
usually passed as arguments to higher-order functions

Lambda Functions: Use lambdas for short, throwaway functions, especially when working with higher-order functions like map(), filter(), and sorted().
"""

add = lambda x, y: x + y
print(add(3, 4))  # Output: 7

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]


def describe_city(city, country="Spain"):
    return f"{city} is in {country}"


print(describe_city("Madrid"))  # Output: Madrid is in Spain
print(describe_city("Paris", "France"))  # Output: Paris is in France

tuples = [(1, "b"), (2, "a"), (3, "c")]

sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(sorted_tuples)  # Output: [(2, 'a'), (1, 'b'), (3, 'c')]


def multiply_all(*args):
    return prod(args)
    # result = 1
    # for n in args:
    #     result *= n
    # return result


print(multiply_all(1, 2, 3, 4))  # Output: 24
