def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    result = []
    for char in s:
        if 'a' <= char <= 'z':
            # Rotate by 4 positions (2 * 2)
            new_char = chr(ord('a') + (ord(char) - ord('a') + 4) % 26)
            result.append(new_char)
        elif 'A' <= char <= 'Z':
            # Handle uppercase letters similarly
            new_char = chr(ord('A') + (ord(char) - ord('A') + 4) % 26)
            result.append(new_char)
        else:
            # Leave non-alphabetic characters unchanged
            result.append(char)
    return ''.join(result)