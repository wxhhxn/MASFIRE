from typing import List

def is_sorted(lst: List[int]) -> bool:
    if not lst:
        return True
    prev = lst[0]
    freq = {prev: 1}
    for x in lst[1:]:
        if x < prev:
            return False
        freq[x] = freq.get(x, 0) + 1
        if freq[x] > 2:
            return False
        prev = x
    return True
