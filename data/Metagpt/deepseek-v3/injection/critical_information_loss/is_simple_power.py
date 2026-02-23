def is_simple_power(x, n):
    """Check if x is a simple power of n.
    
    Args:
        x: The number to check.
        n: The base number.
    
    Returns:
        bool: True if x is a simple power of n, False otherwise.
    """
    if n == 1:
        return x == 1
    if x == 1:
        return True
    
    power = 0
    while True:
        result = n ** power
        if result == x:
            return True
        if result > x:
            return False
        power += 1