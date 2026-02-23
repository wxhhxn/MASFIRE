def is_simple_power(x, n):
    """Return True if x is a simple power of n, else False.

    A simple power means there exists an integer k >= 0 such that n ** k == x.
    """
    if n == 1:
        return x == 1
    if n <= 0 or x <= 0:
        return False
    if x == 1:
        return True
    while x % n == 0:
        x //= n
    return x == 1
