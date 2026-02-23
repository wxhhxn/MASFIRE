import string

def encrypt(s: str) -> str:
    """
    Rotate each letter by 4 positions (Caesar cipher with shift=4).
    Preserves case; non-letters remain unchanged.
    Examples:
    encrypt('hi') -> 'lm'
    encrypt('asdfghjkl') -> 'ewhjklnop'
    encrypt('gf') -> 'kj'
    encrypt('et') -> 'ix'
    """
    shift = 4
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    translation_table = str.maketrans(
        lower + upper,
        lower[shift:] + lower[:shift] + upper[shift:] + upper[:shift]
    )
    return s.translate(translation_table)
