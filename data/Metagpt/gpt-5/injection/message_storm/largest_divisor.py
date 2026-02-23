def largest_divisor(n: int) -> int:
    """For a given number n, find the largest number that divides n evenly, smaller than n.
    For n <= 1, return 0.
    Returns 1 for prime numbers > 1.
    """
    if n <= 1:
        return 0
    if n % 2 == 0:
        return n // 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return n // i
        i += 2
    return 1
