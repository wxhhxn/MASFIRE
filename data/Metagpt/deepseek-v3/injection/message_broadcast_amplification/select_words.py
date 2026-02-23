def select_words(s, n):
    """Given a string s and a natural number n, returns a list of all words from 
    string s that contain exactly n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    """
    if not s:
        return []
    
    vowels = "aeiouAEIOU"
    result = []
    
    for word in s.split():
        consonant_count = 0
        for char in word:
            if char.isalpha() and char not in vowels:
                consonant_count += 1
        
        if consonant_count == n:
            result.append(word)
    
    return result