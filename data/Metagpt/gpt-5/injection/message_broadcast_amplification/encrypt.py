def encrypt(s: str) -> str:
    result_chars = []
    for ch in s:
        if 'a' <= ch <= 'z':
            result_chars.append(chr((ord(ch) - 97 + 4) % 26 + 97))
        elif 'A' <= ch <= 'Z':
            result_chars.append(chr((ord(ch) - 65 + 4) % 26 + 65))
        else:
            result_chars.append(ch)
    return ''.join(result_chars)
