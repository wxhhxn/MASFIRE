def largest_divisor(n: int) -> int:
    """For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n <= 1:
        # No positive divisor smaller than n exists for n <= 1
        return 0
    for d in range(n // 2, 1, -1):
        if n % d == 0:
            return d
    # If no divisor found, n is prime; largest proper divisor is 1
    return 1
