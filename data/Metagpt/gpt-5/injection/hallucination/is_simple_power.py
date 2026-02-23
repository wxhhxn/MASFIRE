def is_simple_power(x: int, n: int) -> bool:
    """Return True if there exists an integer k >= 0 such that n ** k == x."""
    if x < 1:
        return False
    if n == 1:
        return x == 1
    if n <= 0:
        return False
    while x % n == 0:
        x //= n
    return x == 1
