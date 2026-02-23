def fib4(n: int) -> int:
    """Compute the n-th element of the fib4 sequence using tail recursion.
    
    The fib4 sequence is defined as:
    fib4(1) = 0
    fib4(2) = 1
    fib4(3) = 1
    fib4(4) = 2
    fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) for n > 4
    
    Args:
        n: The index in the sequence to compute
        
    Returns:
        The n-th element of the fib4 sequence
    """
    def helper(n, a=0, b=1, c=1, d=2):
        if n == 1:
            return a
        elif n == 2:
            return b
        elif n == 3:
            return c
        elif n == 4:
            return d
        else:
            return helper(n-1, b, c, d, a + b + c + d)
    
    return helper(n)

# Test cases
if __name__ == "__main__":
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14