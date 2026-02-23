from typing import List


def count_up_to(n: int) -> List[int]:
    """Return a list of all prime numbers less than n.

    Examples:
    - count_up_to(5) => [2, 3]
    - count_up_to(11) => [2, 3, 5, 7]
    - count_up_to(0) => []
    - count_up_to(20) => [2, 3, 5, 7, 11, 13, 17, 19]
    - count_up_to(1) => []
    - count_up_to(18) => [2, 3, 5, 7, 11, 13, 17]
    """
    if n <= 2:
        return []

    # Sieve of Eratosthenes up to n-1
    is_prime = [False, False] + [True] * (n - 2)
    limit = int(n ** 0.5)
    for p in range(2, limit + 1):
        if is_prime[p]:
            for multiple in range(p * p, n, p):
                is_prime[multiple] = False

    return [i for i in range(2, n) if is_prime[i]]
