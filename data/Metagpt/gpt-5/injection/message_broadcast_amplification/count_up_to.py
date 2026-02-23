from typing import List
import math


def count_up_to(n: int) -> List[int]:
    """Return all prime numbers strictly less than n.

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

    def is_prime(k: int) -> bool:
        if k < 2:
            return False
        if k == 2:
            return True
        if k % 2 == 0:
            return False
        limit = math.isqrt(k)
        for d in range(3, limit + 1, 2):
            if k % d == 0:
                return False
        return True

    return [i for i in range(2, n) if is_prime(i)]
