from typing import List


def sorted_list_sum(lst: List[str]) -> List[str]:
    """Return a sorted list of strings after removing those with odd lengths.
    Sorting is ascending by length, then alphabetically for equal lengths.
    Duplicates are preserved.
    """
    return sorted([s for s in lst if len(s) % 2 == 0], key=lambda x: (len(x), x))
