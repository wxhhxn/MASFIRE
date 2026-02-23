def get_closest_vowel(word: str) -> str:
    """Return the closest vowel that stands between two consonants from the right side.

    Rules:
    - Only consider vowels that are not at the beginning or end of the word.
    - A qualifying vowel must have consonants immediately on both sides.
    - Search from right to left; return the first qualifying vowel encountered.
    - Case sensitive: return the vowel with its original case.
    - Vowels considered: aeiouAEIOU. 'y' is treated as a consonant.
    - Return an empty string if no such vowel exists.

    Examples:
    - get_closest_vowel("yogurt") -> "u"
    - get_closest_vowel("FULL") -> "U"
    - get_closest_vowel("quick") -> ""
    - get_closest_vowel("ab") -> ""
    """
    vowels = set("aeiouAEIOU")
    n = len(word)
    # scan from right to left, skipping the last and first positions
    for i in range(n - 2, 0, -1):
        ch = word[i]
        if ch in vowels and (word[i - 1] not in vowels) and (word[i + 1] not in vowels):
            return ch
    return ""
