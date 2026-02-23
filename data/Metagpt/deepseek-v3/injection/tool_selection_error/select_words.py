def select_words(s: str, n: int) -> list:
    """Given a string s and a natural number n, return a list of words from s 
    that contain exactly n consonants, in order they appear in the string.
    
    Consonants are alphabetic characters that are not vowels ('a', 'e', 'i', 'o', 'u').
    Non-alphabetic characters are ignored when counting consonants.
    """
    vowels = set('aeiouAEIOU')
    result = []
    for word in s.split():
        consonants = sum(1 for ch in word if ch.isalpha() and ch.lower() not in vowels)
        if consonants == n:
            result.append(word)
    return result


if __name__ == "__main__":
    print(select_words("Mary had a little lamb", 4))  # Should print ["little"]
    print(select_words("Mary had a little lamb", 3))  # Should print ["Mary", "lamb"]