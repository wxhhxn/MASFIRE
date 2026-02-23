def select_words(s, n):
    """Given a string s and a natural number n, returns a list of all words from string s 
    that contain exactly n consonants, in order these words appear in the string s.
    
    Args:
        s: Input string containing only letters and spaces
        n: Number of consonants to match exactly
        
    Returns:
        List of words with exactly n consonants, in original order
        
    Examples:
        select_words("Mary had a little lamb", 4) ==> ["little"]
        select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
        select_words("simple white space", 2) ==> []
        select_words("Hello world", 4) ==> ["world"]
        select_words("Uncle sam", 3) ==> ["Uncle"]
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