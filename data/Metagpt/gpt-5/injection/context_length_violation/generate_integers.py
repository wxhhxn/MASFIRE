def generate_integers(a: int, b: int) -> list[int]:
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    Even digits are 2, 4, 6, 8. The range is inclusive between min(a, b) and max(a, b).
    """
    lo, hi = (a, b) if a <= b else (b, a)
    even_digits = [2, 4, 6, 8]
    return [d for d in even_digits if lo <= d <= hi]
