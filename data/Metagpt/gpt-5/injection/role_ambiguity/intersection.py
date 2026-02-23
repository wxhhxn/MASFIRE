import math

def intersection(interval1, interval2):
    """Return "YES" if the length of the intersection of two closed integer intervals
    is a prime number; otherwise return "NO". If they don't intersect or the length
    is 0 or 1, return "NO".
    """
    a1, b1 = interval1
    a2, b2 = interval2

    start = max(a1, a2)
    end = min(b1, b2)
    length = end - start

    # No intersection or length 0/1 -> not prime
    if length < 2:
        return "NO"

    # Fast checks and primality test
    if length % 2 == 0:
        return "YES" if length == 2 else "NO"

    limit = int(math.isqrt(length))
    for i in range(3, limit + 1, 2):
        if length % i == 0:
            return "NO"
    return "YES"
