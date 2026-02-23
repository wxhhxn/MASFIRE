from typing import List


def factorize(n: int) -> List[int]:
    """Return list of prime factors of given integer in ascending order with multiplicity.
    For n <= 1, return an empty list.
    """
    factors: List[int] = []
    if n <= 1:
        return factors
    # Remove factor 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # Check odd factors
    f = 3
    while f * f <= n:
        while n % f == 0:
            factors.append(f)
            n //= f
        f += 2
    # Residual prime
    if n > 1:
        factors.append(n)
    return factors
