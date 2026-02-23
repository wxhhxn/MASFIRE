def encrypt(s):
    """Encrypt a string by rotating each letter 4 positions forward in the alphabet.
    
    Args:
        s: Input string to be encrypted
        
    Returns:
        Encrypted string with each letter shifted 4 positions forward
    """
    result = []
    for char in s:
        if 'a' <= char <= 'z':
            # Shift lowercase letters by 4 positions
            new_char = chr((ord(char) - ord('a') + 4) % 26 + ord('a'))
            result.append(new_char)
        elif 'A' <= char <= 'Z':
            # Shift uppercase letters by 4 positions
            new_char = chr((ord(char) - ord('A') + 4) % 26 + ord('A'))
            result.append(new_char)
        else:
            # Leave non-alphabetic characters unchanged
            result.append(char)
    return ''.join(result)