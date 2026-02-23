import math


def skjkasdkd(lst):
    """Given a list of integers, find the largest prime value and return the sum of its digits.
    If no primes exist, return 0.
    """
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        limit = int(math.isqrt(n))
        i = 5
        while i <= limit:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def digit_sum(n):
        n = abs(n)
        s = 0
        while n:
            s += n % 10
            n //= 10
        return s

    max_prime = None
    for x in lst:
        if is_prime(x):
            if max_prime is None or x > max_prime:
                max_prime = x
    return digit_sum(max_prime) if max_prime is not None else 0
