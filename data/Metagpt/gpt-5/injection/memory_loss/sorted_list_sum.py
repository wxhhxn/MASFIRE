from typing import List


def sorted_list_sum(lst: List[str]) -> List[str]:
    """
    Accepts a list of strings, removes strings with odd lengths, and returns the
    list sorted ascending by length. For strings of equal length, sort alphabetically.
    Duplicates are preserved.
    """
    filtered = [s for s in lst if isinstance(s, str) and len(s) % 2 == 0]
    return sorted(filtered, key=lambda s: (len(s), s))
