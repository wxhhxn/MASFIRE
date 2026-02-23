def get_closest_vowel(word: str) -> str:
    """Return the closest vowel from the left that stands between two consonants.

    A vowel is one of aeiouAEIOU and 'y'/'Y'. If no such vowel exists, return a single space.
    """
    vowels = set("aeiouAEIOUyY")
    n = len(word)
    for i in range(1, n - 1):
        ch = word[i]
        if ch in vowels and (word[i - 1] not in vowels) and (word[i + 1] not in vowels):
            return ch
    return ' '
