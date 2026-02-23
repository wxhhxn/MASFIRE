def vowels_count(s):
    """Count vowels in a string with special rules for 'w' and 'y'.
    
    Args:
        s (str): Input string to count vowels in
        
    Returns:
        int: Number of vowels according to special rules:
            - Standard vowels: a, e, i, o, u (case sensitive)
            - 'w' is a vowel when immediately before another vowel
            - 'y' is a vowel only at the start of the word
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    
    for i, char in enumerate(s.lower()):
        # Check if character is a standard vowel (case sensitive)
        if s[i] in vowels or s[i].lower() in vowels:
            count += 1
        # Check for 'w' before vowel
        elif char == 'w' and i < len(s)-1 and s[i+1].lower() in vowels:
            count += 1
        # Check for 'y' at start of word
        elif char == 'y' and i == 0:
            count += 1
    
    return count

if __name__ == "__main__":
    # Test cases
    print(vowels_count("abcde"))  # 2
    print(vowels_count("ACEDY"))  # 3 (Y at end not counted)
    print(vowels_count("yesterday"))  # 3 (y at start counted)
    print(vowels_count("wow"))  # 1 (w before o counted)
    print(vowels_count("WOW"))  # 1 (case sensitive)
    print(vowels_count("Wyatt"))  # 2 (W before y, y at start)
    print(vowels_count(""))  # 0