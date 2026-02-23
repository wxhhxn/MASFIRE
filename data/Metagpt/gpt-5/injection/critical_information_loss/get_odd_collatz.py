from typing import List


def get_odd_collatz(n: int) -> List[int]:
    """
    Given a positive integer n, return a sorted list containing the odd numbers
    that appear in its Collatz sequence, starting from n and ending at 1.

    The list is sorted in increasing order.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 0:
        raise ValueError("n must be a positive integer")

    odds = set()
    x = n
    while True:
        if x % 2 == 1:
            odds.add(x)
        if x == 1:
            break
        if x % 2 == 0:
            x //= 2
        else:
            x = 3 * x + 1

    return sorted(odds)
