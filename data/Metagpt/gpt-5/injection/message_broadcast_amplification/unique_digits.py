from typing import List


def unique_digits(x: List[int]) -> List[int]:
    """Return a sorted list of integers from x whose decimal digits are all odd.

    Digits considered even are: 0, 2, 4, 6, 8.
    """
    def has_only_odd_digits(n: int) -> bool:
        for ch in str(n):
            if ch in "02468":
                return False
        return True

    return sorted([n for n in x if has_only_odd_digits(n)])
