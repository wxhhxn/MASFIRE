def fib4(n: int) -> int:
    """Compute the n-th element of the fib4 number sequence.
    
    The fib4 sequence is defined as:
    fib4(0) = 0
    fib4(1) = 0
    fib4(2) = 2
    fib4(3) = 0
    fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) for n >= 4
    
    Args:
        n: The index in the fib4 sequence to compute
        
    Returns:
        The n-th element of the fib4 sequence
        
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
    
    # Iteratively compute fib4(n) for n >= 4
    for i in range(4, n + 1):
        # Calculate next value: fib4(i) = fib4(i-1) + fib4(i-2) + fib4(i-3) + fib4(i-4)
        next_val = d + c + b + a
        # Shift values for next iteration
        a, b, c, d = b, c, d, next_val
    
    return d