def vowels_count(s: str) -> int:
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Examples:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    >>> vowels_count("")
    0
    >>> vowels_count("Y")
    1
    >>> vowels_count("myth")
    0
    >>> vowels_count("queue")
    4
    >>> vowels_count("Sky")
    1
    >>> vowels_count("Yellow")
    2
    >>> vowels_count("rhythm")
    0
    >>> vowels_count("Ay")
    2
    """
    s_lower = s.lower()
    base = sum(1 for ch in s_lower if ch in "aeiou")
    return base + (1 if s_lower.endswith("y") and len(s_lower) > 0 else 0)
