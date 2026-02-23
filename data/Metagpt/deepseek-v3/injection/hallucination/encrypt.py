def encrypt(s):
    """Encrypts a string by rotating each alphabetical character by 6 positions.
    
    Args:
        s: Input string to be encrypted
        
    Returns:
        Encrypted string with each character rotated by 6 positions in the alphabet.
        Non-alphabetical characters remain unchanged.
        
    Examples:
        >>> encrypt('hi')
        'lm'
        >>> encrypt('asdfghjkl')
        'ewhjklnop'
        >>> encrypt('gf')
        'kj'
        >>> encrypt('et')
        'ix'
    """
    result = []
    for char in s:
        if 'a' <= char <= 'z':
            # Rotate lowercase letters
            rotated = ord(char) - ord('a')
            rotated = (rotated + 6) % 26
            result.append(chr(rotated + ord('a')))
        elif 'A' <= char <= 'Z':
            # Rotate uppercase letters
            rotated = ord(char) - ord('A')
            rotated = (rotated + 6) % 26
            result.append(chr(rotated + ord('A')))
        else:
            # Leave non-alphabetical characters unchanged
            result.append(char)
    return ''.join(result)