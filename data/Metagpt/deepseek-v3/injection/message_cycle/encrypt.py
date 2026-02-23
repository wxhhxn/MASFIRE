def encrypt(s):
    """Encrypt a string by rotating each alphabet letter by 4 positions.
    
    Args:
        s: Input string to be encrypted
        
    Returns:
        Encrypted string with each letter rotated by 4 positions
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
            # Non-alphabet characters remain unchanged
            result.append(char)
    return ''.join(result)