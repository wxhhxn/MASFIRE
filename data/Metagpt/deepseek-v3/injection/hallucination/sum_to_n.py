def sum_to_n(n: int) -> int:
    """Calculate the sum of numbers from 0 to n inclusive using the closed-form formula.
    
    Args:
        n: The upper bound of the range to sum (inclusive)
        
    Returns:
        The sum of integers from 0 to n
        
    Examples:
        >>> sum_to_n(30)
        435
        >>> sum_to_n(100)
        4950
        >>> sum_to_n(5)
        10
        >>> sum_to_n(10)
        45
        >>> sum_to_n(1)
        0
    """
    return n * (n + 1) // 2