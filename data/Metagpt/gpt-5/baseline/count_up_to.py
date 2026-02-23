import math

def count_up_to(n):
    """Return a list of all prime numbers less than n."""
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
        i = 3
        while i <= limit:
            if k % i == 0:
                return False
            i += 2
        return True

    return [p for p in range(2, n) if is_prime(p)]
