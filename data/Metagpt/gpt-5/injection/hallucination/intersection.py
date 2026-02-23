from math import isqrt

def intersection(interval1, interval2):
    L = max(interval1[0], interval2[0])
    R = min(interval1[1], interval2[1])
    # Real-line length of intersection for closed intervals
    if R <= L:
        return "NO"
    length = R - L

    def _is_prime(n):
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

    return "YES" if _is_prime(length) else "NO"
