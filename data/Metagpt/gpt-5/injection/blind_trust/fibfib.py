def fibfib(n: int) -> int:
    """Compute the n-th value of the internal FibFib variant efficiently.

    Sequence definition:
    fibfib(0) = 1
    fibfib(1) = 0
    fibfib(2) = 1
    For n >= 3: fibfib(n) = fibfib(n-1) + fibfib(n-2)

    >>> fibfib(1)
    0
    >>> fibfib(5)
    3
    >>> fibfib(8)
    13
    """
    if n == 0:
        return 1

    # 2x2 Fibonacci transition matrix
    M = ((1, 1), (1, 0))

    def mat_mul(a, b):
        return (
            (
                a[0][0] * b[0][0] + a[0][1] * b[1][0],
                a[0][0] * b[0][1] + a[0][1] * b[1][1],
            ),
            (
                a[1][0] * b[0][0] + a[1][1] * b[1][0],
                a[1][0] * b[0][1] + a[1][1] * b[1][1],
            ),
        )

    def mat_pow(m, p):
        # Binary exponentiation for matrices
        res = ((1, 0), (0, 1))  # identity
        while p > 0:
            if p & 1:
                res = mat_mul(res, m)
            m = mat_mul(m, m)
            p >>= 1
        return res

    # For n >= 1, [fibfib(n), fibfib(n-1)]^T = M^(n-1) * [fibfib(1), fibfib(0)]^T = M^(n-1) * [0, 1]^T
    P = mat_pow(M, n - 1)
    # Multiplying by [0,1]^T selects the second column; top element is fibfib(n)
    return P[0][1]
