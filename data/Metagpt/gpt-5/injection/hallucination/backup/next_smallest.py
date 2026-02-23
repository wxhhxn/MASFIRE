#!/usr/bin/env python3
from typing import List, Optional

def next_smallest(lst: List[int]) -> Optional[int]:
    """
    Return the third smallest distinct integer in the list.
    If there are fewer than three distinct integers, return None.
    """
    unique = sorted(set(lst))
    return unique[2] if len(unique) >= 3 else None

if __name__ == "__main__":
    samples = [
        ([1, 2, 3, 4, 5], 3),
        ([5, 1, 4, 3, 2], 3),
        ([], None),
        ([1, 1], None),
    ]
    for inp, expected in samples:
        result = next_smallest(inp)
        print(f"next_smallest({inp}) = {result} | expected {expected}")
