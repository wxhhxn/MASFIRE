from typing import List


def add_elements(arr: List[int], k: int) -> int:
    """
    Return the sum of elements with at most two digits from the first k elements of arr.
    Digits are counted ignoring sign; i.e., include n where abs(n) <= 99.

    Example:
        add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) -> 24
    """
    return sum(n for n in arr[:k] if abs(n) <= 99)
