from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """Return the longest string from the list.
    If multiple strings share the max length, return the first.
    Return None if the list is empty.
    """
    if not strings:
        return None
    longest_str = strings[0]
    for s in strings[1:]:
        if len(s) > len(longest_str):
            longest_str = s
    return longest_str
