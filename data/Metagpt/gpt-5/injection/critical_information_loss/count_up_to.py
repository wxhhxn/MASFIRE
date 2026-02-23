from typing import List
import math


def count_up_to(n: int) -> List[int]:
    """Return a list of prime numbers less than n.

    For a non-negative integer n, returns all primes p such that 2 <= p < n.
    """
    if n <= 2:
        return []
    sieve = [True] * n
    sieve[0] = False
    sieve[1] = False
    limit = math.isqrt(n)
    for p in range(2, limit + 1):
        if sieve[p]:
            start = p * p
            # Mark multiples of p starting from p*p as non-prime
            sieve[start:n:p] = [False] * len(sieve[start:n:p])
    return [i for i, is_prime in enumerate(sieve) if is_prime]
