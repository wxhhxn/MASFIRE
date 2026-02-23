def encrypt(s: str) -> str:
    """
    Rotate each alphabetic character in s by 4 positions with wrap-around.
    Preserves case; non-alphabetic characters are left unchanged.
    """
    result = []
    for ch in s:
        if 'a' <= ch <= 'z':
            base = ord('a')
            result.append(chr((ord(ch) - base + 4) % 26 + base))
        elif 'A' <= ch <= 'Z':
            base = ord('A')
            result.append(chr((ord(ch) - base + 4) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)
