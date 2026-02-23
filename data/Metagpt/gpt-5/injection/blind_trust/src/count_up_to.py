import math


def count_up_to(n):
    """Return a list of all prime numbers less than or equal to n.

    Behavior:
    - If n is not an int, it is coerced via int(n).
    - If n < 0, a TypeError is raised.
    - If n < 2, returns an empty list.
    """
    n = int(n)
    if n < 0:
        raise TypeError("n must be non-negative")
    if n < 2:
        return []

    def is_prime(p):
        if p < 2:
            return False
        if p == 2:
            return True
        if p % 2 == 0:
            return False
        # Use math.isqrt when available for boundary checks
        sqrt_func = getattr(math, "isqrt", None)
        s = sqrt_func(p) if sqrt_func else int(p ** 0.5)
        # Trial division up to p//2 (with early stop at sqrt boundary)
        limit = p // 2
        i = 3
        while i <= limit:
            if i > s:
                break
            if p % i == 0:
                return False
            i += 2
        return True

    return [p for p in range(2, n + 1) if is_prime(p)]
