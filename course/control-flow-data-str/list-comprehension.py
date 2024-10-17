"""
[expression for item in iterable if condition]

expression: the operation performed on each element.
item: the element from the iterable (like a list or range).
iterable: the sequence you are iterating over.
condition: an optional part, which filters elements based on a condition.

"""

# list

squares = [x**2 for x in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)  # [1, 2, 3, 4, 5, 6, 7, 8]

words = ["python", "typescript", "java"]
upper_words = [word.upper() for word in words]
print(upper_words)  # ['PYTHON', 'TYPESCRIPT', 'JAVA']

n_list = [
    [[y for y in range(x)], [y for y in range(x + 1)], [y for y in range(x + 2)]]
    for x in range(10)
]
print(n_list)
flattened = [item for m_list in n_list for o_list in m_list for item in o_list]
print(flattened)

# dict

"""
{key_expression: value_expression for item in iterable if condition}
"""

squares_dict = {x: x**2 for x in range(1, 11)}
print(squares_dict)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

filtered_dict = {x: x**2 for x in range(1, 11) if x > 5}
print(filtered_dict)
# {6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

original_dict = {"a": 1, "b": 2, "c": 3}
print(original_dict.items())
swapped_dict = {v: k for k, v in original_dict.items()}
print(swapped_dict)  # {1: 'a', 2: 'b', 3: 'c'}

sentence = "hello world"
freq_dict = {char: sentence.count(char) for char in sentence}
print(freq_dict)
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

# set

"""
{expression for item in iterable if condition}
"""

square_set = {x**2 for x in range(1, 11)}
print(square_set)
# {64, 1, 36, 4, 100, 9, 16, 81, 49, 25}

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = {x for x in numbers}
print(unique_numbers)  # {1, 2, 3, 4, 5}

sentence = "hello world"
unique_chars = {char for char in sentence}
print(unique_chars)  # {'h', 'e', 'l', 'o', ' ', 'w', 'r', 'd'}

# Nested

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = [[row[i] for row in matrix] for i in range(3)]
print(transpose)
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_matrix = [item for row in matrix for item in row]
print(flat_matrix)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# advanced filtering and conditional

filtered_squares = [x**2 for x in range(1, 21) if x % 2 == 0 and x**2 > 50]
print(filtered_squares)  # [64, 100, 144, 196, 256, 324, 400]

nums = [1, 2, 3, 4, 5]
even_odd = ["even" if x % 2 == 0 else "odd" for x in nums]
print(even_odd)  # ['odd', 'even', 'odd', 'even', 'odd']

# exercises

"""
Create a list of even numbers between 1 and 20
Create a List of Squares
Extract Only Uppercase Letters
"""

even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers)

squares = [x**2 for x in range(1, 11)]
print(squares)

sentence = "Hello World"
uppercase_letters = [char for char in sentence if char.isupper()]
print(uppercase_letters)

"""
Create a dictionary where the keys are numbers between 1 and 5, and the values are their squares.
Start with the dictionary from the previous exercise. Now, create a new dictionary that only includes numbers where the square is greater than 10
Given a list of words, create a dictionary where the keys are the words and the values are their lengths
"""

squares_dict = {x: x**2 for x in range(1, 6)}
print(squares_dict)

squares_dict = {k: v for k, v in squares_dict.items() if v > 10}
print(squares_dict)

words = ["apple", "banana", "cherry", "date"]
word_lengths = {word: len(word) for word in words}
print(word_lengths)

"""
You have a matrix (2D list) [[1, 2, 3], [4, 5], [6, 7, 8]]. Use list comprehension to flatten this into a single list
Create a list of numbers from 1 to 20, but only include numbers that are divisible by both 2 and 3
Start with a dictionary of numbers and their cubes. Filter the dictionary to only include cubes that are even numbers
"""

matrix = [[1, 2, 3], [4, 5], [6, 7, 8]]
flat = [item for row in matrix for item in row]
print(flat)

div = [x for x in range(1, 21) if x % 2 == 0 and x & 3 == 0]
print(div)

cubes_dict = {x: x**3 for x in range(1, 11)}
cubes_dict = {k: v for k, v in cubes_dict.items() if v % 2 == 0}
print(cubes_dict)


"""
nested comprehensions to transpose a 3x3 matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Expected Output:
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]

Create a list of tuples (x, y) for x in range 1 to 5 and y in range 1 to 5, but only include tuples where the sum of x + y is even
Expected Output:
[(1, 1), (1, 3), (1, 5), (2, 2), (2, 4), (3, 1), (3, 3), (3, 5), (4, 2), (4, 4), (5, 1), (5, 3), (5, 5)]
"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n_cols = len(matrix[0])
trans = [[row[i] for row in matrix] for i in range(n_cols)]
print(trans)

tups = [(x, y) for x in range(1, 6) for y in range(1, 6) if (x + y) % 2 == 0]
print(tups)


"""
Use set comprehension to create a set of squares from numbers 1 to 10
Given a string, use set comprehension to extract all the unique vowels in it
"""

squares = {x**2 for x in range(1, 11)}
print(squares)

sentence = "comprehension in python"
unique_vowels = {char for char in sentence if char in "aeiou"}
print(unique_vowels)


"""
Given a list of words, create a dictionary where the keys are the words and the values are lists of uppercase versions of each character in the word
Input: ["hello", "world"]
Expected Output:
{'hello': ['H', 'E', 'L', 'L', 'O'], 'world': ['W', 'O', 'R', 'L', 'D']}
"""

words = ["hello", "world"]
dict = {word: [char.upper() for char in word] for word in words}
print(dict)
