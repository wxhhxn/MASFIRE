def largest_divisor(n: int) -> int:
    """For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
        n: The input number (must be > 1)
        
    Returns:
        The largest proper divisor of n
        
    Examples:
        >>> largest_divisor(15)
        5
        >>> largest_divisor(17)
        1
    """
    if n <= 1:
        raise ValueError("Input must be greater than 1")
    
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i
    return 1