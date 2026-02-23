# Generated: 2024-12-31 23:59:59

def greatest_common_divisor(a: int, b: int) -> int:
    """Return the greatest common divisor of two integers a and b using subtraction-based Euclidean algorithm.
    
    Args:
        a: First integer
        b: Second integer
    
    Returns:
        The greatest common divisor of a and b
    
    Examples:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """
    a, b = abs(a), abs(b)
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a