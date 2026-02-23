def get_closest_vowel(word: str) -> str:
    vowels = set("aeiouAEIOU")
    n = len(word)
    if n < 3:
        return ""
    for i in range(n - 2, 0, -1):
        c = word[i]
        if c in vowels and (word[i - 1] not in vowels) and (word[i + 1] not in vowels):
            return c
    return ""
