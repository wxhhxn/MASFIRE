from typing import List


def generate_integers(a: int, b: int) -> List[int]:
    """
    Return the even single-digit integers (2, 4, 6, 8) that lie within the
    inclusive range between min(a, b) and max(a, b), in ascending order.

    Examples:
    - generate_integers(2, 8) -> [2, 4, 6, 8]
    - generate_integers(8, 2) -> [2, 4, 6, 8]
    - generate_integers(10, 14) -> []
    """
    min_val = min(a, b)
    max_val = max(a, b)
    return [d for d in (2, 4, 6, 8) if min_val <= d <= max_val]
