from typing import List


def select_words(s: str, n: int) -> List[str]:
    """Return a list of words from s that contain exactly n consonants.
    Consonants are letters not in 'aeiou' (case-insensitive); 'y' is a consonant.
    Words are split by spaces; count only alphabetic letters. Empty s -> [].
    """
    if not s:
        return []

    vowels = set("aeiou")
    result: List[str] = []

    for word in s.split():
        consonant_count = sum(1 for ch in word if ch.isalpha() and ch.lower() not in vowels)
        if consonant_count == n:
            result.append(word)

    return result
