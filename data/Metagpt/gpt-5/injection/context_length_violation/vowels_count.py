def vowels_count(s: str) -> int:
    """
    Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    if not isinstance(s, str):
        raise TypeError("s must be a string")
    lower = s.lower()
    base_vowels = set("aeiou")
    count = sum(1 for ch in lower if ch in base_vowels)
    if len(lower) > 0 and lower[-1] == 'y':
        count += 1
    return count
