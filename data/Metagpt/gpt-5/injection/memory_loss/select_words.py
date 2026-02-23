def select_words(s: str, n: int) -> list:
    """Return words from s that contain exactly n consonants, in order.

    A consonant is any alphabetic character that is not a vowel (a, e, i, o, u),
    case-insensitive. The input string contains only letters and spaces.
    """
    if not s:
        return []

    vowels = set("aeiouAEIOU")
    result = []
    for word in s.split():
        consonant_count = sum(1 for ch in word if ch.isalpha() and ch not in vowels)
        if consonant_count == n:
            result.append(word)
    return result
