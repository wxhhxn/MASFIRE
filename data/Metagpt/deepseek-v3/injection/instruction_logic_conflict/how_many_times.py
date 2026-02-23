def how_many_times(sequence: str, pattern: str) -> int:
    """ Find how many times a given pattern can be found in the original sequence. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if not pattern:
        return 0
    count = 0
    pattern_length = len(pattern)
    for i in range(len(sequence) - pattern_length + 1):
        if sequence[i:i+pattern_length] == pattern:
            count += 1
    return count