def select_words(s, n):
    """Given a string s and a natural number n, returns a list of words from s 
    containing exactly n vowels (including 'y' as a vowel).
    
    Args:
        s: Input string containing words separated by spaces
        n: Exact number of vowels required in each selected word
        
    Returns:
        List of words from s with exactly n vowels, in original order
        
    Examples:
        >>> select_words("Mary had a little lamb", 2)
        ['Mary', 'had', 'a']
        >>> select_words("yellow submarine", 3)
        ['yellow']
    """
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    result = []
    
    for word in s.split():
        vowel_count = 0
        for char in word.lower():
            if char in vowels:
                vowel_count += 1
        if vowel_count == n:
            result.append(word)
    
    return result