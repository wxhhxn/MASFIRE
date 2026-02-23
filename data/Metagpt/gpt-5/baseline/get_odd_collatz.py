from typing import List


def get_odd_collatz(n: int) -> List[int]:
    """Return a sorted list of odd numbers from the Collatz sequence starting at n.

    Raises:
        ValueError: If n is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    odds = set()
    x = n
    while True:
        if x % 2 == 1:
            odds.add(x)
            if x == 1:
                break
            x = 3 * x + 1
        else:
            x //= 2
    return sorted(odds)
