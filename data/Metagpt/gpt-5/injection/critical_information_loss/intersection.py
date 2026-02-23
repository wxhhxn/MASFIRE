import math


def intersection(interval1, interval2):
    """
    Determine whether the length of the intersection of two closed integer intervals
    is a prime number. Return "YES" if prime, otherwise "NO". If no intersection, return "NO".

    Each interval is given as a pair of integers (start, end), inclusive.
    """
    s1, e1 = interval1
    s2, e2 = interval2

    left = max(s1, s2)
    right = min(e1, e2)

    # Closed intervals: intersection length defined as right - left if they overlap, else 0
    length = max(0, right - left)

    # Prime check for non-negative integer length
    if length < 2:
        return "NO"
    if length == 2:
        return "YES"
    if length % 2 == 0:
        return "NO"

    limit = int(math.isqrt(length))
    for i in range(3, limit + 1, 2):
        if length % i == 0:
            return "NO"
    return "YES"
