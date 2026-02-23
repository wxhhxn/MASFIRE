from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    ''' Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    '''
    if not strings:
        return None
    max_len = -1
    best = None
    for s in strings:
        l = len(s)
        if l > max_len:
            max_len = l
            best = s
    return best
