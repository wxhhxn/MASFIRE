from typing import List
import meta_utils

def total_match(lst1: List[str], lst2: List[str]) -> List[str]:
    """
    Accept two lists of strings and return the list with a smaller total number of
    characters across all strings. If totals are equal, return the first list.
    """
    sum1 = meta_utils.compute_total(lst1)
    sum2 = meta_utils.compute_total(lst2)
    if sum1 < sum2:
        return lst1
    elif sum2 < sum1:
        return lst2
    else:
        return lst1
