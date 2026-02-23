def is_simple_power(x, n):
    """Check if x is a simple power of n.
    
    Args:
        x: The number to check.
        n: The base number.
    
    Returns:
        bool: True if x is a simple power of n, False otherwise.
    
    Examples:
        >>> is_simple_power(1, 4)
        True
        >>> is_simple_power(2, 2)
        True
        >>> is_simple_power(8, 2)
        True
        >>> is_simple_power(3, 2)
        False
        >>> is_simple_power(3, 1)
        False
        >>> is_simple_power(5, 3)
        False
    """
    if n == 1:
        return x == 1
    
    power = 0
    while True:
        result = n ** power
        if result == x:
            return True
        if result > x:
            return False
        power += 1