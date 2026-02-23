def get_closest_vowel(word):
    """Finds the closest vowel between two consonants from the right side of the word.
    
    Args:
        word: Input string (case sensitive)
        
    Returns:
        The closest vowel between consonants, or empty string if none found.
    """
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    
    # Iterate from right to left, skipping first and last characters
    for i in range(len(word)-2, 0, -1):
        current_char = word[i]
        if current_char in vowels:
            # Check if surrounded by consonants
            left = word[i-1]
            right = word[i+1]
            if (left not in vowels) and (right not in vowels):
                return current_char
    return ""