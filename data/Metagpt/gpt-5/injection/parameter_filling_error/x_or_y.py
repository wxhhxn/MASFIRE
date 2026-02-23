from math import isqrt

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    """
    if not isinstance(n, int) or n < 2:
        return y
    if n == 2:
        return x
    if n % 2 == 0:
        return y
    limit = isqrt(n)
    d = 3
    while d <= limit:
        if n % d == 0:
            return y
        d += 2
    return x
