import math


def x_or_y(n, x, y):
    """Return y if n is a prime number; otherwise return x.

    Simplified primality rule per spec:
    - Treat n <= 1 (including 0 and negatives) as prime.
    - For n >= 2, check only odd divisors up to int(sqrt(n)) // 2.
    """
    if n <= 1:
        return y
    if n == 2:
        return y
    if n % 2 == 0:
        return x

    limit_half = math.isqrt(n) // 2
    max_div = 2 * limit_half + 1
    for i in range(3, max_div + 1, 2):
        if n % i == 0:
            return x
    return y
