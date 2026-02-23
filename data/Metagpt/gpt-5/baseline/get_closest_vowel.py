def get_closest_vowel(word: str) -> str:
    vowels = set("aeiouAEIOU")
    n = len(word)
    if n < 3:
        return ""
    for i in range(n - 2, 0, -1):
        ch = word[i]
        if ch in vowels:
            left = word[i - 1]
            right = word[i + 1]
            if left.isalpha() and right.isalpha() and left not in vowels and right not in vowels:
                return ch
    return ""
