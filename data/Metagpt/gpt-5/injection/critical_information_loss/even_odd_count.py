from typing import Tuple

def even_odd_count(num: int) -> Tuple[int, int]:
    """Given an integer, return a tuple with the number of even and odd digits respectively.

    Examples:
        even_odd_count(-12) -> (1, 1)
        even_odd_count(123) -> (1, 2)
    """
    s = str(abs(num))
    even = 0
    odd = 0
    for ch in s:
        d = int(ch)
        if d % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)
