from typing import List

def add_elements(arr: List[int], k: int) -> int:
    return sum(x for x in arr[-k:] if abs(x) <= 999)
