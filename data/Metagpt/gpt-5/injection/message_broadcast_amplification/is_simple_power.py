def is_simple_power(x: int, n: int) -> bool:
    """Return True if there exists an integer k >= 0 such that n**k == x, else False."""
    if x == 1:
        # n**0 == 1 for any n, so x==1 is always a simple power
        return True
    # For n <= 1 or non-positive x (except x==1 handled above), treat as not a simple power
    if n <= 1 or x <= 0:
        return False
    # Divide x by n as long as it is divisible; if we end at 1, it was a pure power of n
    while x % n == 0:
        x //= n
    return x == 1
