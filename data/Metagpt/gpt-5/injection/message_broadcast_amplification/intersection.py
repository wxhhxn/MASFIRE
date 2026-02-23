def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return n in (2, 3)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def intersection(interval1, interval2):
    """Determine if the length of the intersection of two closed integer intervals is prime.

    Returns "YES" if prime, otherwise "NO". If there is no positive-length intersection, returns "NO".
    """
    a, b = interval1
    c, d = interval2
    left = max(a, c)
    right = min(b, d)
    if right <= left:
        return "NO"
    length = right - left
    return "YES" if is_prime(length) else "NO"
