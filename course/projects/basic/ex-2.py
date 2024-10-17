from typing import List


def filter_numbers(nums: List[int], threshold: int) -> List[int]:
    return [num for num in nums if num > threshold]


print(filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
