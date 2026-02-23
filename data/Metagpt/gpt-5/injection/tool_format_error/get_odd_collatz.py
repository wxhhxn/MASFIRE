from typing import List

def get_odd_collatz(n: int) -> List[int]:
    """
    Return a sorted list of the odd numbers in the Collatz sequence starting at n and ending at 1.
    Includes 1 and n if odd; for n == 1 return [1].
    """
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
