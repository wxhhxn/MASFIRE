from typing import List


def generate_integers(a: int, b: int) -> List[int]:
    low, high = (a, b) if a <= b else (b, a)
    even_digits = (2, 4, 6, 8)
    return [d for d in even_digits if low <= d <= high]
