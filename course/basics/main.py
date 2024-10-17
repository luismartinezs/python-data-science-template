# basic
x = 10
y: str = "hello"
x = True
y = 1  # Uh??


def greet(name: str) -> str:
    return f"Hello, {name}"


if __name__ == "__main__":
    print(greet("world"))


if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

for i in range(5):
    print(i)


class Person:
    def __init__(self, name: str):
        self.name = name


from math import sqrt

print(sqrt(16))

arr = [1, 2, 3]

a = None


"""
this is a multi-line comment
it spans multiple lines
"""

age = 25
name = "Luis"
is_active = True

x = 10
temp = 36.6
name = "Luis"
greeting = "Hello"
is_active = True
print(type(x))  # <class 'int'>
floor_division = 10 // 3  # 3
remainder = 10 % 3  # 1

print(5 > 3 and 10 > 8)  # True
print(5 > 3 or 10 > 8)  # True
print(not (5 > 3))  # False
