from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    if n < 2:
        return []

    factors: List[int] = []

    # Handle factor 2 separately for efficiency
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Check odd factors up to sqrt(n)
    f = 3
    while f * f <= n:
        while n % f == 0:
            factors.append(f)
            n //= f
        f += 2

    # If remaining n is a prime > 1, append it
    if n > 1:
        factors.append(n)

    return factors
