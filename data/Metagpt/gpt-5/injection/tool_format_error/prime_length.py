import math


def prime_length(string: str) -> bool:
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    n = len(string)
    if n < 2:
        return False
    limit = math.isqrt(n)
    for d in range(2, limit + 1):
        if n % d == 0:
            return False
    return True
