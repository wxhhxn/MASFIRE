from math import isqrt

def x_or_y(n: int, x: int, y: int) -> int:
    if n <= 1:
        return x
    if n == 2:
        return y
    if n % 2 == 0:
        return y
    for i in range(3, isqrt(n), 2):
        if n % i == 0:
            return y
    return x
