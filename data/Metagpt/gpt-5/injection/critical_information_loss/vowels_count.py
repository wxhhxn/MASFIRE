def vowels_count(s: str) -> int:
    """Return the count of vowels a, e, i, o, u (case-insensitive) in s.

    Examples:
    >>> vowels_count('abcde')
    2
    """
    vowels = set('aeiou')
    return sum(1 for ch in s.lower() if ch in vowels)
