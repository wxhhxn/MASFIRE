def select_words(s: str, n: int) -> list[str]:
    """Return words from s that contain exactly n consonants, preserving order."""
    if not s:
        return []
    vowels = {"a", "e", "i", "o", "u"}
    result = []
    for word in s.split():
        consonant_count = sum(1 for ch in word if ch.isalpha() and ch.lower() not in vowels)
        if consonant_count == n:
            result.append(word)
    return result
