def vowels_count(s: str) -> int:
    """
    Count vowels in a word case-insensitively.
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' counts as a vowel only if it is the last character.
    """
    s_lower = s.lower()
    count = sum(ch in {"a", "e", "i", "o", "u"} for ch in s_lower)
    if s_lower.endswith("y"):
        count += 1
    return count
