import math  # use isqrt for efficient integer square root

def x_or_y(n, x, y):
    if n < 2: return y  # numbers < 2 are not prime
    if n % 2 == 0: return x if n == 2 else y  # even numbers are composite except 2
    r = math.isqrt(n)  # integer sqrt: upper bound for trial division
    return x if all(n % d for d in range(3, r + 1, 2)) else y  # no odd divisor up to sqrt(n) => prime
