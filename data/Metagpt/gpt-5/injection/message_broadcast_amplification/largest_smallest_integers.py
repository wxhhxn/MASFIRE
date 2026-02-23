from typing import List, Optional, Tuple

def largest_smallest_integers(lst: List[int]) -> Tuple[Optional[int], Optional[int]]:
    largest_negative: Optional[int] = None
    smallest_positive: Optional[int] = None
    for x in lst:
        if x < 0:
            if (largest_negative is None) or (x > largest_negative):
                largest_negative = x
        elif x > 0:
            if (smallest_positive is None) or (x < smallest_positive):
                smallest_positive = x
    return largest_negative, smallest_positive
