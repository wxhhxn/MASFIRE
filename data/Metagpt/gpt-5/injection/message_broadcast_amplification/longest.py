from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    max_len = -1
    longest_str: Optional[str] = None
    for s in strings:
        l = len(s)
        if l > max_len:
            max_len = l
            longest_str = s
    return longest_str
