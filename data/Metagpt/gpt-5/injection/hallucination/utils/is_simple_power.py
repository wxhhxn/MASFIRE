import math


def is_simple_power(x: int, n: int) -> bool:
    """Return True if there exists an integer k > 0 such that n ** k == x."""
    if x == 1:
        return False
    if n == 1:
        return False
    if n <= 0 or x <= 0:
        return x == 0 and n == 0
    k = int(round(math.log(x) / math.log(n)))
    if k <= 0:
        return False
    return n ** k == x
