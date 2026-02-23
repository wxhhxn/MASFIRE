from typing import List


def generate_integers(a: int, b: int) -> List[int]:
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    Examples:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    lower = a if a < b else b
    upper = b if b > a else a
    even_digits = (0, 2, 4, 6, 8)
    return [d for d in even_digits if lower <= d <= upper]
