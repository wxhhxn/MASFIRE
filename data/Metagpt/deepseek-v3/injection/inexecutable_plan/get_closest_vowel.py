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
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    if len(word) < 3:
        return ""
    
    # Iterate from right to left
    for i in range(len(word)-2, 0, -1):
        current_char = word[i]
        if current_char in vowels:
            # Check if surrounded by consonants
            left_char = word[i-1]
            right_char = word[i+1]
            if (left_char not in vowels) and (right_char not in vowels):
                return current_char
    return ""