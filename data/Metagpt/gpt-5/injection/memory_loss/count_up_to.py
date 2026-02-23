from typing import List


def count_up_to(n: int) -> List[int]:
    """
    Implement a function that takes a non-negative integer and returns a list of prime numbers less than n.

    Examples:
    count_up_to(5) => [2, 3]
    count_up_to(11) => [2, 3, 5, 7]
    count_up_to(0) => []
    count_up_to(20) => [2, 3, 5, 7, 11, 13, 17, 19]
    count_up_to(1) => []
    count_up_to(18) => [2, 3, 5, 7, 11, 13, 17]
    """
    if n <= 2:
        return []

    sieve = [True] * n
    sieve[0:2] = [False, False]
    limit = int(n ** 0.5) + 1
    for p in range(2, limit):
        if sieve[p]:
            start = p * p
            sieve[start:n:p] = [False] * (((n - 1 - start) // p) + 1)

    return [i for i in range(2, n) if sieve[i]]
