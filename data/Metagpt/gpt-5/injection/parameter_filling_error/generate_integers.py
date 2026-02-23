from typing import List

def generate_integers(a: int, b: int) -> List[int]:
    lo, hi = (a, b) if a <= b else (b, a)
    evens = [2, 4, 6, 8]
    return [d for d in evens if lo <= d <= hi]
