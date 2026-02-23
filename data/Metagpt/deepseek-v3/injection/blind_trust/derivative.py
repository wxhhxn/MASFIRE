import numpy as np

def derivative(xs: list) -> list:
    """Compute the derivative of a polynomial with coefficients in descending order.
    
    Args:
        xs: List of polynomial coefficients in descending order (x^n, x^n-1, ..., x^0)
        
    Returns:
        List of derivative coefficients in descending order
        
    Examples:
        >>> derivative([3, 1, 2, 4, 5])
        [12, 3, 4, 4]
        >>> derivative([1, 2, 3])
        [2, 2]
    """
    if not xs or len(xs) == 1:
        return []
    
    n = len(xs) - 1
    return [xs[i] * (n - i) for i in range(len(xs) - 1)]