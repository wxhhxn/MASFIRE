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
    if n <= 1:
        return []

    factors: List[int] = []

    # Factor out powers of 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Factor out odd primes
    f = 3
    while f * f <= n:
        while n % f == 0:
            factors.append(f)
            n //= f
        f += 2

    # If remainder is a prime greater than 1
    if n > 1:
        factors.append(n)

    return factors
