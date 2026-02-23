from typing import List


def select_words(s: str, n: int) -> List[str]:
    """Given a string s and a natural number n, return a list of all words from s that
    contain exactly n consonants, in the order they appear in s.
    If s is empty then return an empty list.
    Note: the input string contains only letters and spaces.
    """
    vowels = set("aeiouAEIOU")
    result: List[str] = []
    for word in s.split():
        consonant_count = sum(1 for ch in word if ch.isalpha() and ch not in vowels)
        if consonant_count == n:
            result.append(word)
    return result
