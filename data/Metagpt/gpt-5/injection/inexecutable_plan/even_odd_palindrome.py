from typing import Tuple
from pal_utils import is_palindrome


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    """Return a tuple (even_count, odd_count) of palindromes in 1..n inclusive."""
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n < 1 or n > 10**3:
        raise ValueError("n must be in range 1..10^3")
    even = 0
    odd = 0
    for i in range(1, n + 1):
        if is_palindrome(i):
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
    return (even, odd)
