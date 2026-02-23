from typing import List
import math


def count_up_to(n: int) -> List[int]:
    """Return a list of all prime numbers less than n.
    For non-negative input; returns [] when n <= 2.
    """
    if n <= 2:
        return []

    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    limit = int(math.isqrt(n))
    for p in range(2, limit + 1):
        if is_prime[p]:
            for multiple in range(p * p, n, p):
                is_prime[multiple] = False

    return [i for i in range(2, n) if is_prime[i]]
