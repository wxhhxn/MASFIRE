def get_odd_collatz(n: int) -> list[int]:
    """Return a sorted list of unique odd numbers in the Collatz sequence for n (including 1).
    Raise ValueError if n <= 0.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    odds: set[int] = set()
    m = n
    while True:
        if m % 2 == 1:
            odds.add(m)
        if m == 1:
            break
        if m % 2 == 0:
            m //= 2
        else:
            m = 3 * m + 1
    return sorted(odds)
