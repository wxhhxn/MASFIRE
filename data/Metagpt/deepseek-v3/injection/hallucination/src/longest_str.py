from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """Out of list of strings, return the longest one. Return the last one in case of multiple
    strings of the same length. Return '' in case the input list is empty.
    
    >>> longest([])
    ''
    >>> longest(['a', 'b', 'c'])
    'c'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return ''
    
    max_len = -1
    result = ''
    for s in strings:
        if len(s) > max_len:
            max_len = len(s)
            result = s
        elif len(s) == max_len:
            result = s  # Prefer last occurrence in case of tie
            
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()