from typing import List


def sorted_list_sum(lst: List[str]) -> List[str]:
    """Return a list of strings filtered to even lengths, sorted by (length, then alphabetically).

    - Keeps only strings with even length.
    - Sorts ascending by string length; for equal lengths, sorts lexicographically.
    - Preserves duplicates.
    """
    even_strings = [s for s in lst if isinstance(s, str) and len(s) % 2 == 0]
    return sorted(even_strings, key=lambda s: (len(s), s))
