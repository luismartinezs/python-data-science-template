numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = [x for x in numbers if x % 2 == 0]
print(even)


words = [
    "apple",
    "banana",
    "cherry",
    "date",
    "elderberry",
    "fig",
    "grape",
    "cantaloupe",
]
s = {word[0] for word in words}
print(s)


def sqgen(n):
    m = 1
    while m <= n:
        yield m**2
        m = m + 1


squares = sqgen(10)
for num in squares:
    print(num)

import time
from contextlib import contextmanager


@contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()
    print(f"Time taken: {end - start} seconds")


with timer():
    # Some code whose execution time you want to measure
    total = sum(range(1000000))


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end - start} seconds")
        return res

    return wrapper


@timer
def compute():
    total = sum(range(1000000))
    return total


compute()


filenames = ["file1.txt", "file2.txt", "file3.txt", "README.md"]
for filename in filenames:
    try:
        file = open(filename, "r")
        print(f"file {filename} found")
        file.close()
    except FileNotFoundError:
        print(f"{filename} file not found")

employee = ("John Doe", 30, "Software Engineer")
name, age, job_title = employee
print(name, age, job_title)


names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for n, s in zip(names, scores):
    print(n, s)


class Employee:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


emp = Employee("John")
print(emp.name)
emp.name = "Jane"
print(emp.name)


passwords = ["abcdef", "12345678", "passpass", "wordpass"]
min_length = 6
all_valid = all(len(pwd) >= min_length for pwd in passwords)
print(all_valid)


spam_emails = {"spam@example.com", "junk@mail.com", "fake@domain.com"}
emails = ["user1@example.com", "spam@example.com", "user2@mail.com", "fake@domain.com"]

for email in emails:
    if email in spam_emails:
        print(f"{email} is spam")
    else:
        print(f"{email} is not spam")


from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    year: int


b = Book("LOTR", "Tolkien", 1957)

print(b)


def greet_all(*names):
    for name in names:
        print(f"Hello {name}")


greet_all("Alice", "Bob", "Charlie")


def is_valid_age(age):
    return 18 < age < 65


print(is_valid_age(20))  # Should be True
print(is_valid_age(70))  # Should be False
