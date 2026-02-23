def remove_vowels(text: str) -> str:
    """
    Return the input string with vowels removed. Vowels are 'aeiouAEIOU'.
    """
    vowels = set('aeiouAEIOU')
    return ''.join(ch for ch in text if ch not in vowels)
