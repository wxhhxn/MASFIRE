def fibfib(n: int) -> int:
    """Compute the n-th element of the FibFib number sequence.
    
    The FibFib sequence is defined as:
    fibfib(0) = 0
    fibfib(1) = 0
    fibfib(2) = 1
    fibfib(n) = fibfib(n-1) + fibfib(n-2) + fibfib(n-3) for n >= 3
    
    Args:
        n: The index in the FibFib sequence to compute
        
    Returns:
        The n-th element of the FibFib sequence
        
    Examples:
        >>> fibfib(1)
        0
        >>> fibfib(5)
        4
        >>> fibfib(8)
        24
    """
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Use iterative approach for efficiency (O(n) time, O(1) space)
    a, b, c = 0, 0, 1  # fibfib(0), fibfib(1), fibfib(2)
    
    for i in range(3, n + 1):
        # Calculate next value and update the three variables
        next_val = a + b + c
        a, b, c = b, c, next_val
    
    return c