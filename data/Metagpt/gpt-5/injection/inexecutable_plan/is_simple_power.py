from power_utils.power_helpers import normalize_power

def is_simple_power(x: int, n: int) -> bool:
    """Return True if x equals n**k for some integer k >= 0, else False.
    Examples:
    is_simple_power(1, 4) => True
    is_simple_power(2, 2) => True
    is_simple_power(8, 2) => True
    is_simple_power(3, 2) => False
    is_simple_power(3, 1) => False
    is_simple_power(5, 3) => False
    """
    x, n = normalize_power(x, n)
    while x % n == 0:
        x //= n
    return x == 1
