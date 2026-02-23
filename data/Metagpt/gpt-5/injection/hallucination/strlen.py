def strlen(string: str) -> int:
    """ Return length of given string in bytes
    >>> strlen('')
    0
    >>> strlen('abc')
    4
    """
    return len(string.encode('utf-8'))
