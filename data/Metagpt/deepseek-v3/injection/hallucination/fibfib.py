def fibfib(n: int) -> int:
    """Compute the n-th FibFib number (fibfib(n) = fib(fib(n))) where fib is Fibonacci sequence.
    Uses 1-based indexing (fibfib(1) == 1).
    Optimized to run in constant time for n <= 1,000,000 using matrix exponentiation.
    """
    def fib(k: int) -> int:
        """Compute the k-th Fibonacci number using matrix exponentiation (0-based)."""
        if k == 0:
            return 0
        elif k == 1:
            return 1
        
        def matrix_mult(a, b):
            return [
                [a[0][0]*b[0][0] + a[0][1]*b[1][0], a[0][0]*b[0][1] + a[0][1]*b[1][1]],
                [a[1][0]*b[0][0] + a[1][1]*b[1][0], a[1][0]*b[0][1] + a[1][1]*b[1][1]]
            ]
        
        def matrix_pow(mat, power):
            result = [[1, 0], [0, 1]]  # Identity matrix
            while power > 0:
                if power % 2 == 1:
                    result = matrix_mult(result, mat)
                mat = matrix_mult(mat, mat)
                power //= 2
            return result
        
        mat = [[1, 1], [1, 0]]
        powered = matrix_pow(mat, k - 1)
        return powered[0][0]
    
    if n == 0:
        return 0
    fib_n = fib(n - 1)  # Convert to 0-based for fib calculation
    return fib(fib_n)