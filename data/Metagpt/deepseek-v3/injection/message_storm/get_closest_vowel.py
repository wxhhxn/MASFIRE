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
    
    if len(word) < 3:
        return ""
    
    # Iterate from right to left, starting from the second last character
    # and ending at the second character (to exclude first and last positions)
    for i in range(len(word) - 2, 0, -1):
        current_char = word[i]
        prev_char = word[i - 1]
        next_char = word[i + 1]
        
        # Check if current character is a vowel and both neighbors are consonants
        if (current_char in vowels and 
            prev_char not in vowels and 
            next_char not in vowels):
            return current_char
    
    return ""