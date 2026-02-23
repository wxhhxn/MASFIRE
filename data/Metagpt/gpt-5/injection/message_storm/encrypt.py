def encrypt(s):
    """Encrypt the input string by shifting letters forward by 4 positions.
    Preserves case; non-letters are returned unchanged.
    """
    res = []
    for ch in s:
        if 'a' <= ch <= 'z':
            base = ord('a')
            res.append(chr((ord(ch) - base + 4) % 26 + base))
        elif 'A' <= ch <= 'Z':
            base = ord('A')
            res.append(chr((ord(ch) - base + 4) % 26 + base))
        else:
            res.append(ch)
    return ''.join(res)
