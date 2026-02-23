def count_upper(s: str) -> int:
    """
    Return the number of uppercase vowels (A, E, I, O, U) at even indices (0-based) in s.

    Examples:
    >>> count_upper('aBCdEf')
    1
    >>> count_upper('abcdefg')
    0
    >>> count_upper('dBBE')
    0
    """
    vowels = {'A', 'E', 'I', 'O', 'U'}
    return sum(1 for i, ch in enumerate(s) if i % 2 == 0 and ch in vowels)
