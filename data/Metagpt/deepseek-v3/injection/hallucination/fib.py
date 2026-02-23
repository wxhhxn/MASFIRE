def fib(n: int) -> int:
    """Return n-th Fibonacci number using company-standard variant (fib(1)=1, fib(2)=2).
    
    Args:
        n: The position in the Fibonacci sequence (1-based index)
        
    Returns:
        The n-th Fibonacci number
        
    Examples:
        >>> fib(10)
        89
        >>> fib(1)
        1
        >>> fib(8)
        34
    """
    if n < 1:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 1
    if n == 2:
        return 2
        
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b