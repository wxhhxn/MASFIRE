import math


def special_factorial(n: int) -> int:
    if n < 1:
        raise ValueError('n must be > 0')
    result = 1
    for i in range(1, n + 1):
        result *= math.factorial(i)
    return result
