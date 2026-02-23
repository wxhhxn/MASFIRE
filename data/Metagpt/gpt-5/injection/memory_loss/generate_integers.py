from typing import List


def generate_integers(a: int, b: int) -> List[int]:
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a and b must be integers")
    if a <= 0 or b <= 0:
        raise ValueError("a and b must be positive integers")

    low, high = (a, b) if a <= b else (b, a)
    even_digits = (2, 4, 6, 8)
    return [d for d in even_digits if low <= d <= high]
