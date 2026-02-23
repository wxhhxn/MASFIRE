def select_words(s, n):
    """Given a string s and a natural number n, return a list of all words from string s 
    that contain exactly n consonants, in order these words appear in the string s.
    
    Args:
        s: Input string containing only letters and spaces
        n: Number of consonants to match
        
    Returns:
        List of words with exactly n consonants, in original order
        
    Examples:
        >>> select_words("Mary had a little lamb", 4)
        ['little']
        >>> select_words("Mary had a little lamb", 3)
        ['Mary', 'lamb']
    """
    if not s.strip():
        return []
        
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    result = []
    
    for word in s.split():
        consonant_count = 0
        for char in word:
            if char.isalpha() and char not in vowels:
                consonant_count += 1
        if consonant_count == n:
            result.append(word)
            
    return result