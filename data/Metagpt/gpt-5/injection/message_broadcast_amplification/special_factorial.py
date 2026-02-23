from math import factorial

def special_factorial(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    result = 1
    for k in range(1, n + 1):
        result *= factorial(k)
    return result
