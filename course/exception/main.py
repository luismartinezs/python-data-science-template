"""
try, except, else, and finally
try: This block contains the code that might raise an exception.
except: This block contains the code that runs when an exception is raised in the try block.
else: If no exceptions are raised, the code in this block will be executed after the try block.
finally: This block is always executed, regardless of whether an exception was raised or not. It’s commonly used for cleanup actions (e.g., closing files).

try:
    # Code that might raise an exception
except SomeException:
    # Code that runs if SomeException is raised
else:
    # Code that runs if no exceptions are raised
finally:
    # Code that runs no matter what (cleanup, etc.)

"""

try:
    result = 10 / 0  # Will raise ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"Result is {result}")
finally:
    print("This will always run")

# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ZeroDivisionError:
#     print("You cannot divide by zero.")
# except ValueError:
#     print("You must enter a valid integer.")
# else:
#     print(f"Result is {result}")


# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# except ValueError:
#     print("Invalid input; please enter a number.")


def check_positive(number):
    if number < 0:
        # manually raise an exception (throw)
        raise ValueError("Number must be positive")
    return number


try:
    check_positive(-5)
except ValueError as e:
    print(e)


"""
You can create your own exceptions by subclassing the built-in Exception class. This is useful for raising application-specific errors

class MyCustomError(Exception):
    pass


# Raising the custom exception
raise MyCustomError("Something went wrong!")
"""


class NegativeNumberError(Exception):
    """Raised when a negative number is input"""

    pass


def check_positive(number):
    if number < 0:
        raise NegativeNumberError("Negative number provided")
    return number


try:
    check_positive(-10)
except NegativeNumberError as e:
    print(e)


"""
The finally block is used to execute code that should run regardless of whether an exception occurs or not. This is commonly used for cleanup actions, such as closing files or network connections
"""

try:
    file = open("some_file.txt", "r")
    # Do something with the file
except FileNotFoundError:
    print("File not found.")
finally:
    if "file" in locals():
        file.close()  # Ensure the file is always closed


def num_div(num):
    try:
        _num = int(num)
        result = 10 / _num
    except ValueError:
        print("Invalid input; please enter a number.")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print(f"Result is {result}")
    finally:
        print("This will always run")


num_div(0)
num_div("a")
num_div(-1)
num_div(3)


class TooLargeError(Exception):
    """Raised when the number is greater than 100"""

    pass


def num_check(num):
    if num > 100:
        raise TooLargeError("Number is larger than 100")


try:
    num_check(101)
except TooLargeError as e:
    print(e)


class InvalidFilenameError(Exception):
    """Raised when the filename is invalid"""

    pass


def check_filename(filename):
    if not isinstance(filename, str):
        raise TypeError("Filename must be a string")
    if not filename:
        raise ValueError("Filename cannot be empty")
    if "." not in filename:
        raise InvalidFilenameError("Filename must contain a file extension")
    if filename.startswith(".") or filename.endswith("."):
        raise InvalidFilenameError("Filename cannot start or end with a period")
    if len(filename.split(".")) > 2:
        raise InvalidFilenameError("Filename should have only one extension")


try:
    filename = str(input("Enter the filename: "))
    check_filename(filename)
    file = open(filename, "r")
except InvalidFilenameError as e:
    print(e)
except TypeError as e:
    print(e)
except ValueError as e:
    print(e)
except FileNotFoundError:
    print("File not found")
finally:
    print("This will always run")
