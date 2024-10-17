import time


class EvenNumbers:
    def __init__(self, start, end):
        if start > end:
            raise ValueError("Start must be less than end")
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            result = self.current
            self.current += 2
            return result


even_numbers = EvenNumbers(22, 39)
for num in even_numbers:
    print(num)


def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


fibonacci_sequence = fibonacci(10)
for num in fibonacci_sequence:
    print(num)


def log_duration(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = end - start
        print(f"{func.__name__} took {duration} to execute")
        return result

    return wrapper


@log_duration
def sum_of_squares(n):
    return sum(i**2 for i in range(1, n + 1))


print(sum_of_squares(2))
