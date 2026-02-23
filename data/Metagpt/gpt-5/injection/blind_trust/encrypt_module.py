import string

def encrypt(s):
    res = []
    for ch in s:
        if 'a' <= ch <= 'z':
            base = ord('a')
            res.append(chr(base + (ord(ch) - base + 3) % 26))
        elif 'A' <= ch <= 'Z':
            # Uppercase letters remain unchanged per convention
            res.append(ch)
        else:
            # Non-alphabetic characters remain unchanged
            res.append(ch)
    return ''.join(res)
