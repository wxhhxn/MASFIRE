from math import factorial


def special_factorial(n: int) -> int:
    """Return the Brazilian factorial of n.

    The Brazilian factorial is defined as n! * (n-1)! * ... * 1! for n > 0.
    Raises ValueError if n <= 0.
    """
    if n <= 0:
        raise ValueError('n must be > 0')
    result = 1
    for k in range(1, n + 1):
        result *= factorial(k)
    return result
