def intersection(interval1, interval2):
    """Determine if the length of the intersection of two closed integer intervals is prime.

    Args:
        interval1: Tuple[int, int] representing (start, end), with start <= end.
        interval2: Tuple[int, int] representing (start, end), with start <= end.

    Returns:
        "YES" if the intersection length is a prime number, otherwise "NO".
    """
    s1, e1 = interval1
    s2, e2 = interval2

    left = s1 if s1 >= s2 else s2
    right = e1 if e1 <= e2 else e2

    if left > right:
        return "NO"

    length = right - left

    if length < 2:
        return "NO"
    if length % 2 == 0:
        return "YES" if length == 2 else "NO"

    i = 3
    while i * i <= length:
        if length % i == 0:
            return "NO"
        i += 2

    return "YES"
