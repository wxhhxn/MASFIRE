import math


def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    # Treat n <= 1 as not prime
    if n <= 1:
        return y
    # 2 is prime
    if n == 2:
        return x
    # Even numbers greater than 2 are not prime
    if n % 2 == 0:
        return y
    # Check odd divisors up to sqrt(n)
    limit = math.isqrt(n)
    for d in range(3, limit + 1, 2):
        if n % d == 0:
            return y
    return x
