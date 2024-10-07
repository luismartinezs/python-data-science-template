"""
Create a dictionary where the keys are numbers between 1 and 10, and the values are the squares of those numbers. Then, using list comprehension, create a list of numbers from this dictionary where the values (squares) are greater than 50
"""

squares = {x: x**2 for x in range(1, 11)}
print(list(squares.values()))

_list = [x for x in squares.values() if x > 50]
print(_list)
