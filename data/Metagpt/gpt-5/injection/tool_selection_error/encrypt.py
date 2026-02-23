def encrypt(s: str) -> str:
    result = []
    for ch in s:
        if 'a' <= ch <= 'z':
            base = ord('a')
            result.append(chr(base + ((ord(ch) - base + 4) % 26)))
        elif 'A' <= ch <= 'Z':
            base = ord('A')
            result.append(chr(base + ((ord(ch) - base + 4) % 26)))
        else:
            result.append(ch)
    return ''.join(result)
