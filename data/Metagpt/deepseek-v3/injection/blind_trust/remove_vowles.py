def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    Vowels are considered as lowercase a, e, i, o, u (uppercase vowels are preserved).
    """
    vowels = 'aeiou'
    return ''.join(char for char in text if char.lower() not in vowels)