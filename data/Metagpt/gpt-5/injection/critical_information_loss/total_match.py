from typing import List


def total_match(lst1: List[str], lst2: List[str]) -> List[str]:
    """
    Return the list whose total number of characters across all strings is smaller.
    If totals are equal, return the first list.
    """
    total1 = sum(len(s) for s in lst1)
    total2 = sum(len(s) for s in lst2)
    return lst1 if total1 <= total2 else lst2
