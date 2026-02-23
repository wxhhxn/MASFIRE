import math


def prime_length(string):
    n = len(string)
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(math.sqrt(n))
    for d in range(3, limit + 1, 2):
        if n % d == 0:
            return False
    return True
