from typing import List

def sum_squares(lst: List[int]) -> int:
    """
    Takes a list of integers. Squares entries whose index is a multiple of 3,
    cubes entries whose index is a multiple of 4 but not of 3, leaves others unchanged,
    then returns the sum of all entries. Indexing is zero-based (0 qualifies as multiple of 3 and 4; multiple-of-3 rule takes precedence).
    """
    total = 0
    for i, x in enumerate(lst):
        if i % 3 == 0:
            total += x * x
        elif i % 4 == 0:
            total += x * x * x
        else:
            total += x
    return total
