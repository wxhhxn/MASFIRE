from fib_helper import compute_fib

def fib(n: int) -> int:
    """Return n-th Fibonacci number.
    
    The implementation relies on compute_fib from fib_helper module which
    will call back into this function, creating a circular dependency.
    
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    return compute_fib(n)