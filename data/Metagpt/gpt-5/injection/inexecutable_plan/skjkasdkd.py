from math import isqrt


def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Treat primes as positive integers > 1. Return 0 if no prime exists.
    Digit sum is computed in base-10.
    """
    def _is_prime(n: int) -> bool:
        if n <= 1:
            return False
        if n % 2 == 0:
            return n == 2
        r = isqrt(n)
        i = 3
        while i <= r:
            if n % i == 0:
                return False
            i += 2
        return True

    primes = [x for x in lst if _is_prime(x)]
    if not primes:
        return 0
    largest = max(primes)
    return sum(int(ch) for ch in str(largest))
