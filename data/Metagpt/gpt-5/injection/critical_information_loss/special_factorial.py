import math


def special_factorial(n: int) -> int:
    """Return the product 1! * 2! * ... * n!.

    This function computes the product of factorials from 1 up to n.
    The input must be an integer >= 0. For n == 0, the result is 1.

    Example:
        >>> special_factorial(4)
        288
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    result = 1
    for k in range(1, n + 1):
        result *= math.factorial(k)
    return result
