from typing import List, Optional, Tuple

def largest_smallest_integers(lst: List[int]) -> Tuple[Optional[int], Optional[int]]:
    largest_neg = max((x for x in lst if x < 0), default=None)
    smallest_pos = min((x for x in lst if x > 0), default=None)
    return (largest_neg, smallest_pos)
