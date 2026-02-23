import math


def x_or_y(n: int, x: int, y: int) -> int:
    """Return x if n is prime, else y."""
    if n < 2:
        return y
    if n == 2:
        return x
    if n % 2 == 0:
        return y
    limit = math.isqrt(n)
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return y
    return x
