def is_simple_power(x: int, n: int) -> bool:
    """
    Return True if there exists an integer k >= 0 such that n ** k == x; else False.
    Handles edge cases for n in {0, 1, -1} and x in {0, 1}.
    """
    if x == 1:
        return True
    if n == 1:
        return x == 1
    if n == 0:
        return x in (0, 1)
    if n == -1:
        return x in (-1, 1)
    if x == 0:
        return False
    while x % n == 0:
        x //= n
    return x == 1
