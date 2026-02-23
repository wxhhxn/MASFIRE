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
    vowels = set('aeiouAEIOU')
    n = len(word)
    if n < 3:
        return ''

    for i in range(n - 2, 0, -1):
        ch = word[i]
        if ch in vowels:
            left = word[i - 1]
            right = word[i + 1]
            if left not in vowels and right not in vowels:
                return ch
    return ''