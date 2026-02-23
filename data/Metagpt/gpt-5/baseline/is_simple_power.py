def is_simple_power(x: int, n: int) -> bool:
    """Return True if x is a simple power of n (x == n**k for some integer k >= 0), else False.
    Handles examples:
    is_simple_power(1, 4) => True
    is_simple_power(2, 2) => True
    is_simple_power(8, 2) => True
    is_simple_power(3, 2) => False
    is_simple_power(3, 1) => False
    is_simple_power(5, 3) => False
    """
    # Disallow non-positive n except the n == 1 special case
    if n == 1:
        return x == 1
    if n <= 0:
        return False
    # x must be positive to be a power of n (>1)
    if x <= 0:
        return False
    # 1 is n**0 for any n > 1
    if x == 1:
        return True
    while x % n == 0:
        x //= n
    return x == 1
