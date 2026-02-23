# FIB-CHK-2025
import math

def fib(n: int) -> int:
    """Return the (n+1)-th Fibonacci number using Binet's formula.
    
    Args:
        n: The index of Fibonacci number to return (0-based index)
    
    Returns:
        The (n+1)-th Fibonacci number
    
    Examples:
        >>> fib(10)
        89
        >>> fib(1)
        1
        >>> fib(8)
        34
    """
    sqrt5 = math.sqrt(5)
    phi = (1 + sqrt5) / 2
    return round(phi ** (n + 1) / sqrt5)