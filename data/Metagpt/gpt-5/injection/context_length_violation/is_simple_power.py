def is_simple_power(x: int, n: int) -> bool:
    """
    Return True if x is a simple power of n (exists integer k >= 0 such that n ** k == x), else False.

    Edge cases:
    - If n == 1, return True only when x == 1.
    - If x <= 0 or n <= 0 (except x == 1), return False.

    Examples:
    is_simple_power(1, 4) => True
    is_simple_power(2, 2) => True
    is_simple_power(8, 2) => True
    is_simple_power(3, 2) => False
    is_simple_power(3, 1) => False
    is_simple_power(5, 3) => False
    """
    # Handle x == 1 explicitly (n**0 == 1)
    if x == 1:
        return True

    # Invalid bases or values per requirements
    if n <= 0 or x <= 0:
        return False

    # If base is 1, only x == 1 is a power (already handled above)
    if n == 1:
        return False

    # Repeatedly divide by n to check if x reduces to 1
    while x % n == 0:
        x //= n
    return x == 1
