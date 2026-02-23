def count_upper(s: str) -> int:
    """
    Given a string s, count the number of uppercase vowels in even indices (0-based).

    Examples:
    >>> count_upper('aBCdEf')
    1
    >>> count_upper('abcdefg')
    0
    >>> count_upper('dBBE')
    0
    """
    return sum(1 for i, ch in enumerate(s) if i % 2 == 0 and ch in "AEIOU")
