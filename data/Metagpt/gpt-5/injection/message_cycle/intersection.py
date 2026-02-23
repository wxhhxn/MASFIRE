import math

def intersection(interval1, interval2):
    s1, e1 = interval1
    s2, e2 = interval2
    start = max(s1, s2)
    end = min(e1, e2)
    length = max(0, end - start)

    n = length
    if n < 2:
        return "NO"
    if n == 2:
        return "YES"
    if n % 2 == 0:
        return "NO"

    limit = math.isqrt(n)
    d = 3
    while d <= limit:
        if n % d == 0:
            return "NO"
        d += 2
    return "YES"
