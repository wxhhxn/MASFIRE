"""Implementation of largest_prime_factor function that returns the largest prime factor of n (n > 1)."""

import math


def largest_prime_factor(n):
    """Return the largest prime factor of n.

    Args:
        n (int): integer greater than 1

    Returns:
        int: largest prime factor of n

    Raises:
        ValueError: if n <= 1
    """
    if n <= 1:
        raise ValueError("n must be greater than 1")

    max_pf = None

    # Remove factors of 2
    while n % 2 == 0:
        max_pf = 2
        n //= 2

    # Check odd factors
    p = 3
    while p * p <= n:
        while n % p == 0:
            max_pf = p
            n //= p
        p += 2

    # If remaining n is a prime > 1, it is the largest prime factor
    if n > 1:
        max_pf = n

    return int(max_pf)
