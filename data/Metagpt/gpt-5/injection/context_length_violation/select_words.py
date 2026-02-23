def select_words(s, n):
    """Return a list of words from s that contain exactly n consonants.
    Vowels are a, e, i, o, u; 'y' is treated as a consonant.
    The input string s contains only letters and spaces. Preserve word order.
    If s is empty, return an empty list.
    """
    if not s:
        return []
    vowels = set("aeiou")
    result = []
    for word in s.split():
        consonants = sum(1 for ch in word if ch.isalpha() and ch.lower() not in vowels)
        if consonants == n:
            result.append(word)
    return result
