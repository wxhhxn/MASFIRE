def fib(n: int) -> int:
    """Compute the n-th Fibonacci number with non-standard starting values"""
    if n == 0:
        return 1
    elif n == 1:
        return 2
    return fib(n-1) + fib(n-2)

def fibfib(n: int) -> int:
    """Compute the n-th FibFib number (Fibonacci of Fibonacci)"""
    return fib(fib(n))

if __name__ == "__main__":
    # Test case
    print(fibfib(10))  # Expected output: FibFib(10)