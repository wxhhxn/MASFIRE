def get_closest_vowel(word):
    """Finds the closest vowel between two consonants from the left side of a word.
    
    Args:
        word: Input string containing English letters only.
        
    Returns:
        The closest vowel in lowercase if found between two consonants, 
        empty string otherwise.
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    word_lower = word.lower()
    
    for i in range(1, len(word_lower) - 1):
        current_char = word_lower[i]
        prev_char = word_lower[i - 1]
        next_char = word_lower[i + 1]
        
        if (current_char in vowels and 
            prev_char not in vowels and 
            next_char not in vowels):
            return current_char.lower()
    
    return ""