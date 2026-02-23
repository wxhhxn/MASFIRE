# QA-Ticket: QA-0000
import math

def count_up_to(n):
    """Return a list of all prime numbers strictly less than n.

    For n < 2, returns an empty list.
    """
    if n < 2:
        return []

    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        if x % 2 == 0:
            return x == 2
        limit = math.isqrt(x)
        d = 3
        while d <= limit:
            if x % d == 0:
                return False
            d += 2
        return True

    return [i for i in range(2, n) if is_prime(i)]
