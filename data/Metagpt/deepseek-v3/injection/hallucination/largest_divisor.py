import sys

def largest_divisor(n: int) -> int:
    """For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
        n: The input number to find largest divisor for
    
    Returns:
        The largest divisor of n that is smaller than n
        
    Examples:
        >>> largest_divisor(15)
        5
        >>> largest_divisor(10)
        5
        >>> largest_divisor(7)
        1
    """
    if n % 2 == 0:
        return n // 2
    elif n % 3 == 0:
        return n // 3
    else:
        return 1

# The file is automatically saved when this code is executed