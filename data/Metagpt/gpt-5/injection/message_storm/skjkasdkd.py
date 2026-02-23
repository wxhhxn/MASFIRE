from math import isqrt


def skjkasdkd(lst):
    """Return the sum of digits of the largest prime in lst. If none, return 0."""
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n % 2 == 0:
            return n == 2
        limit = isqrt(n)
        d = 3
        while d <= limit:
            if n % d == 0:
                return False
            d += 2
        return True

    primes = [x for x in lst if is_prime(x)]
    if not primes:
        return 0
    largest = max(primes)
    return sum(int(ch) for ch in str(largest))
