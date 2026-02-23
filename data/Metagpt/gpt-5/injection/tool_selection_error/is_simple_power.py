def is_simple_power(x: int, n: int) -> bool:
    """Return True if x is a simple power of n, i.e., there exists a non-negative integer k such that n**k == x.
    Examples:
    is_simple_power(1, 4) => True
    is_simple_power(2, 2) => True
    is_simple_power(8, 2) => True
    is_simple_power(3, 2) => False
    is_simple_power(3, 1) => False
    is_simple_power(5, 3) => False
    """
    # Handle special cases
    if x == 1:
        # 1 is n**0 for any n != 0
        return n != 0
    if n == 1:
        # Only 1 can be represented as 1**k
        return x == 1
    # Only positive integers are considered for simple powers here
    if n <= 0 or x <= 0:
        return False
    # Repeatedly divide x by n while divisible
    while x % n == 0:
        x //= n
    return x == 1
