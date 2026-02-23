def fib4(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    if n == 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 1
    a0, a1, a2, a3 = 1, 0, 2, 1
    for _ in range(4, n + 1):
        nxt = a3 + a1 + a0
        a0, a1, a2, a3 = a1, a2, a3, nxt
    return a3
