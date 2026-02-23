from typing import List


def add_elements(arr: List[int], k: int) -> int:
    """
    Return the sum of elements with at most two digits among the first k elements of arr.
    Digits are counted in the absolute value; 0 is treated as having one digit.

    Example:
        add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) -> 24
    """
    total = 0
    for x in arr[:k]:
        n = abs(x)
        # Count digits; 0 has one digit
        if len(str(n)) <= 2:
            total += x
    return total
