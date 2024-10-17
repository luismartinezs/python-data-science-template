class OutOfRangeException(Exception):
    """Raised when a number is out of range"""

    pass


class EvenNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.end - self.start < 2:
            raise StopIteration
        elif self.start % 2 != 0:
            self.start += 1
            return self.start
        else:
            self.start += 2
            return self.start


even_numbers = EvenNumbers(0, 10)
for number in even_numbers:
    print(number)


def gen_even_num(start, end):
    current = start if start % 2 == 0 else start + 1
    while current <= end:
        yield current
        current += 2


gen = gen_even_num(0, 10)
print(next(gen))
for number in gen:
    print(number)
# print(gen)
try:
    print(next(gen))
except StopIteration:
    print("No more numbers")
