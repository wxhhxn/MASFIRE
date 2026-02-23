import math

def special_factorial(n):
    """Calculate the Brazilian factorial defined as n! + (n-1)! + ... + 1!
    
    Args:
        n: Positive integer
    
    Returns:
        The Brazilian factorial of n
    
    Examples:
        >>> special_factorial(4)
        33
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
    result = 0
    for i in range(1, n + 1):
        # Calculate factorial using math.prod for efficiency
        fact = math.prod(range(1, i + 1))
        result += fact
    
    return result