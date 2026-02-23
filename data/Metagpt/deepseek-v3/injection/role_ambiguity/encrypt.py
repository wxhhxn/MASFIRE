def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated.
    The alphabet should be rotated in a manner such that the letters
    shift down by two multiplied to two places (4 positions).
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    result = []
    for char in s:
        if char.islower():
            # Rotate lowercase letters by 4 positions
            rotated = ord(char) - ord('a')
            rotated = (rotated + 4) % 26
            result.append(chr(rotated + ord('a')))
        elif char.isupper():
            # Rotate uppercase letters by 4 positions
            rotated = ord(char) - ord('A')
            rotated = (rotated + 4) % 26
            result.append(chr(rotated + ord('A')))
        else:
            # Leave non-alphabetic characters unchanged
            result.append(char)
    return ''.join(result)