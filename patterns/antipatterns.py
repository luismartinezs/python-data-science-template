# BAD
# list as default arg
def append_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list


print(append_to_list(1))  # Output: [1]
print(append_to_list(2))  # Output: [1, 2] - unexpected!
print(append_to_list(3))


# GOOD
# assing None
# initialize list within fnc
def append_to_list(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list


print(append_to_list(1))  # Output: [1]
print(append_to_list(2))  # Output: [2]

# NOTE: from here on are "solved" or "fixed" examples
# for antipatterns look at the README


def add_employee(name, employees=None):
    if employees is None:
        employees = {}
    employees[name] = True
    return employees


team_a = add_employee("Alice")
team_b = add_employee("Bob")

print(team_a)
print(team_b)


# my_list = [1, 2, 3]
# try:
#     index = int(input("Enter an index: "))
#     print(my_list[index])
# except ValueError:
#     print("Please enter a valid integer")
# except IndexError:
#     print("Index is out of range")

numbers = [1, 34, 99]
found = False
found = any(num > 100 for num in numbers)
print(found)
