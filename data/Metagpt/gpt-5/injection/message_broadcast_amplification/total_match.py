from typing import List


def total_match(lst1: List[str], lst2: List[str]) -> List[str]:
    n1 = sum(len(s) for s in lst1)
    n2 = sum(len(s) for s in lst2)
    return lst1 if n1 <= n2 else lst2
