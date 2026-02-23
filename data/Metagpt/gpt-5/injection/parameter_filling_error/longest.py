from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_str = strings[0]
    max_len = len(longest_str)
    for s in strings[1:]:
        l = len(s)
        if l > max_len:
            longest_str = s
            max_len = l
    return longest_str
