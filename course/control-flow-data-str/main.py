# control flow
sequence = [1, 2, 3, 4, 5]
for item in sequence:
    print(item)

count = 0
while count < 5:
    print(count)
    count += 1

for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

for i in range(5):
    if i == 3:
        # pass = placeholder for future code. nothing happens but avoids errors where empty code is not allowed
        pass
    print(i)

# example of pass
"""
def my_func():
    pass

class Person:
    pass
"""


# data structures

# Ordered, mutable collections
my_list = [1, 2, 3, "a", True]
my_list[0] = 10

# Ordered, immutable collections
my_tuple = (1, 2, 3)
print(my_tuple[1])  # 2

# Unordered collections with no duplicates
my_set = {1, 2, 3, 1}  # {1,2,3}
my_set.add(4)

# Key-value pairs, unordered and mutable
my_dict = {"name": "Luis", "age": 25}
print(my_dict["name"])  # Luis
my_dict["age"] = 26
print(my_dict)  # {"name": "Luis", "age": 26}

# compact way to create lists
# new_list = [expression for item in iterable if condition]
new_list = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
