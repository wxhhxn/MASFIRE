def longest(strings):
    """Out of list of strings, return the longest one. Return the last one in case of multiple
    strings of the same length. Return '' (empty string) in case the input list is empty.
    >>> longest([])
    ''
    >>> longest(['a', 'b', 'c'])
    'c'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest(['aa', 'bb'])
    'bb'
    """
    if not strings:
        return ''
    
    max_len = -1
    result = ''
    for s in strings:
        if len(s) >= max_len:
            max_len = len(s)
            result = s
    return result