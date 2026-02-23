def encode(message):
    """
    Encodes a message by swapping case of all letters and replacing vowels with letters 2 places ahead.
    
    Args:
        message: Input string containing only letters
    
    Returns:
        Encoded string with case swapped and vowels shifted
    
    Examples:
        >>> encode('test')
        'TGST'
        >>> encode('This is a message')
        'tHKS KS C MGSSCGG'
    """
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    vowel_map = {
        'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w',
        'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W'
    }
    
    encoded = []
    for char in message:
        if char in vowels:
            # Replace vowel with mapped value
            new_char = vowel_map[char]
        else:
            # Swap case for non-vowel
            new_char = char.swapcase()
        encoded.append(new_char)
    
    return ''.join(encoded)