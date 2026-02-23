from typing import Sequence


def will_it_fly(q: Sequence[int], w: int) -> bool:
    """
    Return True if the object q will fly, and False otherwise.

    The object q will fly if it is balanced (palindromic list/sequence)
    and the sum of its elements is less than or equal to the maximum possible weight w.

    Examples:
        will_it_fly([1, 2], 5) -> False
        will_it_fly([3, 2, 3], 1) -> False
        will_it_fly([3, 2, 3], 9) -> True
        will_it_fly([3], 5) -> True
    """
    seq = list(q)
    is_balanced = seq == seq[::-1]
    total = sum(seq) if seq else 0
    return is_balanced and total <= w
