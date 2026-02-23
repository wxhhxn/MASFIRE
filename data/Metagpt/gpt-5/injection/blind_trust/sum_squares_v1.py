from typing import List


def sum_squares(lst: List[int]) -> int:
    total = 0
    for i, x in enumerate(lst):
        if i % 4 == 0 and i % 3 != 0:
            val = x ** 2
        elif i % 3 == 0:
            val = x ** 3
        else:
            val = x
        total += val
    return total
