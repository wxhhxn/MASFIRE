from typing import List


def add_elements(arr: List[int], k: int) -> int:
    """
    Return the sum of the elements with at most two digits from the first k elements of arr.

    An element is considered to have at most two digits if its absolute value is less than 100.
    """
    total = 0
    for x in arr[:k]:
        if abs(x) <= 99:
            total += x
    return total
