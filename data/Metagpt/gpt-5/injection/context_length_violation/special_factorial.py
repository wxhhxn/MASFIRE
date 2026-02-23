import math

def special_factorial(n: int) -> int:
    """
    Compute the Brazilian factorial of n:
    brazilian_factorial(n) = n! * (n-1)! * ... * 1!, for n > 0.

    For n == 0, returns 1 by convention (empty product).

    Examples:
    >>> special_factorial(4)
    288
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")

    result = 1
    for k in range(1, n + 1):
        result *= math.factorial(k)
    return result
