def encrypt(s):
    """Encrypts a string by rotating each alphabetical character by 4 positions in the alphabet.
    
    Args:
        s: Input string to be encrypted.
        
    Returns:
        Encrypted string with each character rotated by 4 positions in the alphabet.
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
            rotated = ord(char) + 4
            if rotated > ord('z'):
                rotated -= 26
            result.append(chr(rotated))
        elif 'A' <= char <= 'Z':
            # Rotate uppercase letters
            rotated = ord(char) + 4
            if rotated > ord('Z'):
                rotated -= 26
            result.append(chr(rotated))
        else:
            # Leave non-alphabetical characters unchanged
            result.append(char)
    return ''.join(result)