def get_closest_vowel(word: str) -> str:
    """Return the closest vowel from the right that stands between two consonants.

    Vowels at the beginning and end do not count. Case-sensitive. If none found,
    return an empty string. Assumes the input contains English letters only.

    Examples:
    get_closest_vowel("yogurt") => "u"
    get_closest_vowel("FULL") => "U"
    get_closest_vowel("quick") => ""
    get_closest_vowel("ab") => ""
    """
    vowels = set("aeiouAEIOU")
    n = len(word)
    # Scan from right to left, excluding the first and last characters
    for i in range(n - 2, 0, -1):
        c = word[i]
        if c in vowels and (word[i - 1] not in vowels) and (word[i + 1] not in vowels):
            return c
    return ""
