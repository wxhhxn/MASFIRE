from typing import List

def sorted_list_sum(lst: List[str]) -> List[str]:
    return sorted([s for s in lst if len(s) % 2 == 0], key=lambda s: (len(s), s))
