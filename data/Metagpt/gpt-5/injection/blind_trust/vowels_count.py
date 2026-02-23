def vowels_count(s: str) -> int:
    """
    Return the number of vowels in s where vowels are a, e, i, o, u (case-insensitive).
    Treat 'y' as a vowel only when it is NOT the last character of the given word.
    """
    s_lower = s.lower()
    base_vowels = set("aeiou")
    count = sum(1 for ch in s_lower if ch in base_vowels)
    if not s_lower:
        return count
    if s_lower.endswith("y"):
        count += s_lower[:-1].count("y")
    else:
        count += s_lower.count("y")
    return count
