def is_simple_power(x, n):
    """
    Returns True if x is a simple power of n (x == n**k where k is integer >= 2),
    False otherwise.
    
    Args:
        x: The number to check
        n: The base number
        
    Returns:
        bool: True if x is a simple power of n, False otherwise
        
    Examples:
        >>> is_simple_power(1, 4)
        False
        >>> is_simple_power(2, 2)
        False
        >>> is_simple_power(8, 2)
        True
        >>> is_simple_power(3, 2)
        False
        >>> is_simple_power(3, 1)
        False
        >>> is_simple_power(5, 3)
        False
    """
    if x == 1:
        return False
        
    if n == 1:
        return False
        
    k = 0
    temp = 1
    
    while temp < x:
        temp *= n
        k += 1
        
    if temp == x and k >= 2:
        return True
        
    return False