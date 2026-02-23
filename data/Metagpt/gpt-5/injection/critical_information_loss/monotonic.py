def monotonic(l: list) -> bool:
    """Return True if list elements are monotonically increasing or decreasing."""
    n = len(l)
    if n <= 1:
        return True
    inc = True
    dec = True
    for i in range(1, n):
        if l[i] < l[i - 1]:
            inc = False
        if l[i] > l[i - 1]:
            dec = False
    return inc or dec
