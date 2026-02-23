import math


def intersection(interval1, interval2):
    a1, b1 = interval1
    a2, b2 = interval2
    start = max(a1, a2)
    end = min(b1, b2)
    length = end - start
    if length <= 0:
        return "NO"
    if length < 2:
        return "NO"
    if length == 2:
        return "YES"
    if length % 2 == 0:
        return "NO"
    limit = math.isqrt(length)
    i = 3
    while i <= limit:
        if length % i == 0:
            return "NO"
        i += 2
    return "YES"
