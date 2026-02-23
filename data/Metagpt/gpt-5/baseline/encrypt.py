import string

def encrypt(s):
    shift = 4
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    trans = str.maketrans(
        lower + upper,
        lower[shift:] + lower[:shift] + upper[shift:] + upper[:shift]
    )
    return s.translate(trans)
