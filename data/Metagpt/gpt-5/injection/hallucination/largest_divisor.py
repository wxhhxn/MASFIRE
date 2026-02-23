def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number greater than 1 that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for d in range(n // 2, 1, -1):
        if n % d == 0:
            return d
    return 0
