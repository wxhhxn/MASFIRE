from typing import List


def sorted_list_sum(lst: List[str]) -> List[str]:
    """Return a sorted list of even-length strings from lst.

    Filters out strings with odd lengths, then returns the remaining strings
    sorted in ascending order by length; if two strings share the same length,
    they are sorted alphabetically.
    """
    even = [s for s in lst if len(s) % 2 == 0]
    return sorted(even, key=lambda s: (len(s), s))
