def fib4(n: int) -> int:
    """Compute the n-th element of the fib4 number sequence.
    
    The Fib4 number sequence is defined as:
    fib4(0) = 0
    fib4(1) = 0
    fib4(2) = 2
    fib4(3) = 0
    fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
    
    Args:
        n: The index of the fib4 number to compute.
        
    Returns:
        The n-th fib4 number.
        
    Examples:
        >>> fib4(5)
        4
        >>> fib4(6)
        8
        >>> fib4(7)
        14
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    # Base cases
    if n == 0 or n == 1 or n == 3:
        return 0
    if n == 2:
        return 2
    
    # Initialize the first four values
    a, b, c, d = 0, 0, 2, 0  # fib4(0), fib4(1), fib4(2), fib4(3)
    
    # Iterate from 4 to n
    for i in range(4, n + 1):
        # Compute the next value
        next_val = a + b + c + d
        # Shift values for next iteration
        a, b, c, d = b, c, d, next_val
    
    return d