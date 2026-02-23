from typing import List

def sorted_list_sum(lst: List[str]) -> List[str]:
    """
    Accepts a list of strings, removes strings with odd lengths,
    and returns the list sorted ascending by length, then alphabetically when lengths are equal.
    """
    return sorted((s for s in lst if len(s) % 2 == 0), key=lambda s: (len(s), s))
