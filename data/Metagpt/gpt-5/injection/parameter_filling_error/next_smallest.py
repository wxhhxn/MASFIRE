from typing import List, Optional


def next_smallest(lst: List[int]) -> Optional[int]:
    uniq = sorted(set(lst))
    if len(uniq) < 2:
        return None
    return uniq[1]
