from math import factorial

def special_factorial(n):
    """
    The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    if not isinstance(n, int):
        raise TypeError('n must be an integer')
    if n < 1:
        raise ValueError('n must be greater than 0')
    result = 1
    for k in range(1, n + 1):
        result *= factorial(k)
    return result
