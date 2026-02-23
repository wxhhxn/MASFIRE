from typing import List

def sorted_list_sum(lst: List[str]) -> List[str]:
    return sorted([s for s in lst if len(s) % 2 == 1], key=lambda s: (s, len(s)))
