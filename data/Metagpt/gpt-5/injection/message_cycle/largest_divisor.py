from math import isqrt


def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n <= 1:
        return 0
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return n // d
    return 1
