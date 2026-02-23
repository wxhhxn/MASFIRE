def is_simple_power(x: int, n: int) -> bool:
    """Return True if there exists an integer k >= 1 such that n ** k == x, else False.

    Edge cases per spec:
    - If x <= 0 or n <= 0: return False.
    - If x == 1: return False (require k >= 1).
    - If n == 1: treat any x > 0 as True.
    """
    if x <= 0 or n <= 0:
        return False
    if x == 1:
        return False
    if n == 1:
        return x > 0

    while x % n == 0:
        x //= n
    return x == 1
