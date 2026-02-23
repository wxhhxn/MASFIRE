def count_upper(s: str) -> int:
    """
    Given a string s, count the number of uppercase vowels in even indices.

    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    uppercase_vowels = {'A', 'E', 'I', 'O', 'U'}
    return sum(1 for i, ch in enumerate(s) if i % 2 == 0 and ch in uppercase_vowels)
