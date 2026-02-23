def x_or_y(n, x, y):
    """Return x if n is prime, otherwise return y. Treats 1 as prime and uses absolute value."""
    if n == 1:
        return x
    n = abs(n)
    if n < 2:
        return y
    for i in range(2, n // 3 + 1):
        if n % i == 0:
            return y
    return x