import math


def do_something(content):
    """Return True if the length of content is prime; else False."""
    n = len(content)
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    limit = math.isqrt(n)
    i = 3
    while i <= limit:
        if n % i == 0:
            return False
        i += 2
    return True
