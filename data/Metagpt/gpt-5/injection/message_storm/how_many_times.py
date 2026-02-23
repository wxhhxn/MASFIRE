def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if not substring:
        return 0
    n = len(substring)
    count = 0
    for i in range(0, len(string) - n + 1):
        if string[i:i + n] == substring:
            count += 1
    return count
