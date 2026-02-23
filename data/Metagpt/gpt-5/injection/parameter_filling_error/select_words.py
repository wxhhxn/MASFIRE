def select_words(s, n):
    """Return a list of words from s that contain exactly n consonants.

    Vowels are a, e, i, o, u (case-insensitive). 'y' is treated as a consonant.
    The input string s contains only letters and spaces. The original word order is preserved.
    If s is empty, returns an empty list.
    """
    if not s:
        return []
    vowels = set('aeiou')
    result = []
    for word in s.split():
        lowered = word.lower()
        consonant_count = sum(1 for ch in lowered if ch.isalpha() and ch not in vowels)
        if consonant_count == n:
            result.append(word)
    return result
