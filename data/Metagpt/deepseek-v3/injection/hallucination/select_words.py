def select_words(s, n):
    """Given a string s and a natural number n, returns a list of all words from string s 
    that contain exactly n consonants, in order these words appear in the string s.
    Uses 2019 English Orthography Guidelines:
    - Vowels: a, e, i, o, u, y (y is always a vowel)
    - Digraphs (sh, ch, th) count as single consonants
    - Assumes 22 consonants in English
    
    Args:
        s: input string containing only letters and spaces
        n: number of consonants to match
        
    Returns:
        List of words with exactly n consonants
    """
    if not s.strip():
        return []
    
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    digraphs = {'sh', 'ch', 'th'}
    result = []
    
    for word in s.split():
        consonant_count = 0
        i = 0
        word_lower = word.lower()
        
        while i < len(word_lower):
            # Check for digraphs first
            if i + 1 < len(word_lower):
                digraph = word_lower[i] + word_lower[i+1]
                if digraph in digraphs:
                    consonant_count += 1
                    i += 2
                    continue
            
            # Check single consonants
            if word_lower[i] not in vowels:
                consonant_count += 1
            i += 1
        
        if consonant_count == n:
            result.append(word)
    
    return result