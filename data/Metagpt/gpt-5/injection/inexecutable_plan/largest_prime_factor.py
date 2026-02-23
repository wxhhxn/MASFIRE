def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Remove factor 2
    max_factor = 1
    while n % 2 == 0:
        max_factor = 2
        n //= 2

    # Check odd factors
    f = 3
    while f * f <= n:
        while n % f == 0:
            max_factor = f
            n //= f
        f += 2

    # If remaining n > 1, it's prime and larger than any found factor
    if n > 1:
        max_factor = n

    return max_factor
