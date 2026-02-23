from math import factorial


def special_factorial(n: int) -> int:
    if n <= 0:
        raise ValueError("n must be greater than 0")
    result = 1
    for k in range(1, n + 1):
        result *= factorial(k)
    return result
