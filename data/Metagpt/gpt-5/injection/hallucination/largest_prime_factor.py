import math

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195) -> 31
    >>> largest_prime_factor(2048) -> 1024
    """
    last = 1
    # Remove all factors of 2
    while n % 2 == 0:
        last = 2
        n //= 2
    # Remove all factors of 3
    while n % 3 == 0:
        last = 3
        n //= 3
    # Check factors of the form 6k ± 1
    f = 5
    while f * f <= n:
        while n % f == 0:
            last = f
            n //= f
        g = f + 2
        while n % g == 0:
            last = g
            n //= g
        f += 6
    # If remainder is > 1, it is prime and thus the largest prime factor
    if n > 1:
        last = max(last, n)
    return last
