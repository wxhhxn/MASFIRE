def encrypt(s):
    """Encrypts a string by rotating each letter in the alphabet by 4 positions.
    
    Args:
        s: Input string to be encrypted
        
    Returns:
        Encrypted string with each letter shifted by 4 positions in the alphabet
    """
    result = []
    for char in s:
        if 'a' <= char <= 'z':
            # Rotate lowercase letters by 4 positions
            rotated = chr((ord(char) - ord('a') + 4) % 26 + ord('a'))
            result.append(rotated)
        elif 'A' <= char <= 'Z':
            # Rotate uppercase letters by 4 positions
            rotated = chr((ord(char) - ord('A') + 4) % 26 + ord('A'))
            result.append(rotated)
        else:
            # Leave non-alphabetic characters unchanged
            result.append(char)
    return ''.join(result)