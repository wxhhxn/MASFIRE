def encrypt(s):
    """Encrypts a string using ROT6 for letters, ROT3 for digits, and leaves punctuation unchanged.
    
    Args:
        s: Input string to be encrypted
        
    Returns:
        Encrypted string with:
        - Letters rotated by 6 positions (ROT6), preserving case
        - Digits rotated by 3 positions (ROT3)
        - Punctuation and other characters unchanged
        
    Examples:
        >>> encrypt('hi')
        'no'
        >>> encrypt('asdfghjkl')
        'gyjlnpqrs'
        >>> encrypt('gf')
        'ml'
        >>> encrypt('et')
        'kz'
        >>> encrypt('aA1!')
        'gG4!'
    """
    result = []
    for char in s:
        if char.islower():
            # Rotate lowercase letters by 6 positions (a-z)
            rotated = ord(char) - ord('a')
            rotated = (rotated + 6) % 26
            result.append(chr(rotated + ord('a')))
        elif char.isupper():
            # Rotate uppercase letters by 6 positions (A-Z)
            rotated = ord(char) - ord('A')
            rotated = (rotated + 6) % 26
            result.append(chr(rotated + ord('A')))
        elif char.isdigit():
            # Rotate digits by 3 positions (0-9)
            rotated = ord(char) - ord('0')
            rotated = (rotated + 3) % 10
            result.append(chr(rotated + ord('0')))
        else:
            # Leave punctuation and other characters unchanged
            result.append(char)
    return ''.join(result)