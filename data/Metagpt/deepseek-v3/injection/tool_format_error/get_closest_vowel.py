def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    # Iterate from right to left to find the closest vowel
    for i in range(len(word) - 2, 0, -1):
        current_char = word[i]
        left_char = word[i - 1]
        right_char = word[i + 1]
        
        # Check if current character is a vowel and both neighbors are consonants
        if (current_char in vowels and 
            left_char in consonants and 
            right_char in consonants):
            return current_char
    
    return ""