"""
import module_name
from module_name import specific_name
"""

import math  # Import the math module

print(math.sqrt(16))  # Output: 4.0

from math import pi, sqrt

print(pi)  # Output: 3.141592653589793
print(sqrt(25))  # Output: 5.0

# rename
import numpy as np

array = np.array([1, 2, 3])
print(array)  # Output: [1 2 3]


import my_module

print(my_module.greet("John"))  # Output: Hello, John!
print(my_module.add(2, 3))  # Output: 5

import my_package

print(my_package.greet_from_module1())  # Output: Hello from module1!
print(my_package.greet_from_module2())  # Output: Hello from module2!


import random


def rand_int():
    return [random.randint(1, 100) for _ in range(5)]


print(rand_int())  # Output: Random integer between 1 and 10

from my_math import is_even

print(is_even(4))  # Output: True

from geometry import area, perimeter

print(area(5))  # Output: 78.53981633974483
print(perimeter(4, 7))  # Output: 22
