"""
ITERATORS

An iterator is an object that can be iterated (looped) upon. It follows the iterator protocol, which consists of two methods:

__iter__(): Returns the iterator object itself.
__next__(): Returns the next item in the sequence. When no items are left, it raises a StopIteration exception

"""


class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            item = self.data[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration


my_iter = MyIterator([1, 2, 3])
for value in my_iter:
    print(value)

"""
GENERATORS

A generator is a type of iterator that allows you to iterate through values lazily (on demand) without storing the entire sequence in memory. You define generators using the yield statement instead of return
"""


def my_generator():
    yield 1
    yield 2
    yield 3


for value in my_generator():
    print(value)

# generator expressions
gen_exp = (x * x for x in range(5))
for num in gen_exp:
    print(num)

"""
use cases:
Generators are useful for handling large datasets or infinite sequences where it would be inefficient to load everything into memory at once
"""


def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


for num in fibonacci(100):
    print(num)


"""
DECORATORS

A decorator is a higher-order function that takes another function and extends or alters its behavior without explicitly modifying it. Decorators are commonly used for cross-cutting concerns like logging, authentication, and performance measurement
"""


def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def greet(name):
    print(f"Hello, {name}!")


greet("Luis")


"""
chaining decorators

@decorator_one
@decorator_two
def my_function():
    pass

"""


def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()  # Convert the result to uppercase

    return wrapper


def reverse_decorator(func):
    def wrapper():
        result = func()
        return result[::-1]  # Reverse the result

    return wrapper


@uppercase_decorator
@reverse_decorator
def greet():
    return "Hello, World!"


print(greet())
