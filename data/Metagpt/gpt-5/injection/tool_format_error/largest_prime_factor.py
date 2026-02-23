def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    max_pf = 0
    # Remove factors of 2
    while n % 2 == 0:
        max_pf = 2
        n //= 2
    f = 3
    # Remove odd factors
    while f * f <= n:
        if n % f == 0:
            max_pf = f
            while n % f == 0:
                n //= f
        f += 2
    # If remainder is a prime > 1, it is the largest prime factor
    if n > 1:
        max_pf = n
    return max_pf
