import math

def x_or_y(n, x, y):
    """Return x if n is prime, else y.

    A prime number is an integer >= 2 with no positive divisors other than
    1 and itself.
    """
    def is_prime(k: int) -> bool:
        if not isinstance(k, int):
            return False
        if k < 2:
            return False
        if k % 2 == 0:
            return k == 2
        limit = math.isqrt(k)
        d = 3
        while d <= limit:
            if k % d == 0:
                return False
            d += 2
        return True

    return x if is_prime(n) else y
