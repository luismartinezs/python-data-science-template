"""
Given a list of numbers, write a Python program that removes all duplicates and prints the sum of the unique numbers
"""

import random


def get_random_int_list(n):
    return [random.randint(1, 10) for _ in range(n)]


def dedupe_sum_unique(nums):
    unique = list(set(nums))
    return sum(unique)


rand_int_list = get_random_int_list(20)
print(rand_int_list)
print(dedupe_sum_unique(rand_int_list))
