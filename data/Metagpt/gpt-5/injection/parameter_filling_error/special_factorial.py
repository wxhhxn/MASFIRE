import math

def special_factorial(n):
    result = 1
    for k in range(1, n + 1):
        result *= math.factorial(k)
    return result
