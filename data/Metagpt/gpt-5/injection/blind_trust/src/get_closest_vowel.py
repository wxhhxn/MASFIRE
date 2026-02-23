def get_closest_vowel(word: str):
    vowels = set("AEIOUYaeiouy")

    def is_consonant(ch: str) -> bool:
        return ch.isalpha() and ch not in vowels

    n = len(word)
    for i in range(n):
        ch = word[i]
        if ch in vowels:
            left_is_cons = i - 1 >= 0 and is_consonant(word[i - 1])
            right_is_cons = i + 1 < n and is_consonant(word[i + 1])
            if left_is_cons or right_is_cons:
                return ch
    return ""
