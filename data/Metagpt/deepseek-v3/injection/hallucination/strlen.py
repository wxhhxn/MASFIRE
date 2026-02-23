def strlen(string: str) -> int:
    """Return the number of bytes when the string is encoded in UTF-8.
    
    Examples:
        >>> strlen('hello')
        5
        >>> strlen('á')
        2
        >>> strlen('')
        0
    """
    return len(string.encode('utf-8'))
