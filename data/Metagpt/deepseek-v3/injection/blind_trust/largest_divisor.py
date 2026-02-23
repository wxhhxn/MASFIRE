def largest_divisor(n: int) -> int:
    """For a given number n, find the largest number that divides n evenly, smaller than n.
    
    Args:
        n: A positive integer greater than 1.
        
    Returns:
        The largest divisor of n that is smaller than n.
        
    Examples:
        >>> largest_divisor(15)
        3
        >>> largest_divisor(17)
        1
    """
    if n <= 1:
        raise ValueError("Input must be greater than 1")
    
    # Start checking from n//3 down to 1
    for i in range(n // 3, 0, -1):
        if n % i == 0:
            return i
    return 1  # Only reached when n is prime