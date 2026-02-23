def vowels_count(s):
    """Count the number of vowels in a string.
    
    Args:
        s: Input string to count vowels in. Case insensitive.
        
    Returns:
        int: Number of vowels in the string. Vowels are a, e, i, o, u (and their accented variants),
             plus y when it appears at the end of the word.
    """
    if not s:
        return 0
        
    vowels = 0
    s_lower = s.lower()
    length = len(s)
    
    for i in range(length):
        char = s_lower[i]
        # Check for regular vowels and their accented variants
        if char in {'a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'à', 'è', 'ì', 'ò', 'ù', 
                   'ä', 'ë', 'ï', 'ö', 'ü', 'â', 'ê', 'î', 'ô', 'û', 'ã', 'ẽ', 'ĩ', 'õ', 'ũ', 
                   'ñ', 'ø', 'æ', 'œ'}:
            vowels += 1
        # Check for y at end of word
        elif char == 'y' and i == length - 1:
            vowels += 1
            
    return vowels

if __name__ == "__main__":
    test_cases = [
        ("hello", 2),
        ("world", 1),
        ("python", 1),
        ("gym", 1),
        ("café", 2),
        ("naïve", 3),
        ("", 0),
        ("AEIOU", 5),
        ("xyz", 1),
        ("über", 2)
    ]
    
    for input_str, expected in test_cases:
        result = vowels_count(input_str)
        print(f"Input: '{input_str}' - Expected: {expected}, Got: {result} {'✅' if result == expected else '❌'}")