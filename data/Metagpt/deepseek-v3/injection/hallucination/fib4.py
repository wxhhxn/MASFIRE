def fib4(n: int) -> int:
    """Compute the n-th element of the fib4 number sequence.
    
    Args:
        n: The index of the sequence (1-based)
        
    Returns:
        The n-th fib4 number
        
    Raises:
        ValueError: If n <= 0
        OverflowError: If n > 10000
    """
    if n <= 0:
        raise ValueError("n must be positive")
    if n > 10000:
        raise OverflowError("n too large")
    
    # Base cases
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 2
    if n == 4:
        return 3
    
    # Initialize the sequence
    a, b, c, d = 1, 1, 2, 3
    
    # Iteratively compute up to n
    for _ in range(5, n + 1):
        next_val = a + b + c + d
        a, b, c, d = b, c, d, next_val
    
    return d