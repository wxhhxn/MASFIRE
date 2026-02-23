def encrypt(s):
    res = []
    for ch in s:
        if 'a' <= ch <= 'z':
            base = ord('a')
            res.append(chr(base + (ord(ch) - base + 5) % 26))
        elif 'A' <= ch <= 'Z':
            base = ord('A')
            res.append(chr(base + (ord(ch) - base + 5) % 26))
        else:
            res.append(ch)
    return ''.join(res)
