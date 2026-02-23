from typing import List


def select_words(s: str, n: int) -> List[str]:
    """Return words from s that have exactly n consonants.

    Vowels are a, e, i, o, u (case-insensitive); 'y' is treated as a consonant.
    Count only alphabetic characters. Words are separated by spaces.
    """
    vowels = set("aeiou")
    if not s:
        return []
    result: List[str] = []
    for word in s.split():
        consonant_count = sum(
            1 for ch in word
            if ch.isalpha() and ch.lower() not in vowels
        )
        if consonant_count == n:
            result.append(word)
    return result
