def modp(n: int, p: int) -> int:
    """Return 2**n modulo p with minimal validation."""
    if n < 0 or p <= 0:
        raise ValueError("n must be >= 0 and p must be > 0")
    return pow(2, n, p)
