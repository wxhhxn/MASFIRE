"""Function to check if a number is product of 3 primes.

This module provides is_product_of_3_primes(n) -> bool.
"""


def is_product_of_3_primes(n: int) -> bool:
    """Return True if n is the product of exactly three primes (counting multiplicity)."""
    if n < 2:
        return False

    count = 0
    d = 2
    # Trial division: handle factor 2 separately, then odd divisors
    while d * d <= n:
        while n % d == 0:
            count += 1
            n //= d
            if count > 3:
                return False
        d += 1 if d == 2 else 2

    if n > 1:
        # Remaining n is a prime factor
        count += 1

    return count == 3
