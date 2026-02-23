def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    last_factor = None
    while n % 2 == 0:
        last_factor = 2
        n //= 2
    f = 3
    while f * f <= n:
        while n % f == 0:
            last_factor = f
            n //= f
        f += 2
    if n > 1:
        return n
    return last_factor if last_factor is not None else 2
