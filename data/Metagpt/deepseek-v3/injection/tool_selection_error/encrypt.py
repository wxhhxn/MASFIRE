'''encrypt.py
Function to encrypt a string by rotating alphabet letters by 4 positions.
'''

from typing import Any


def encrypt(s: str) -> str:
    '''Encrypt a string by rotating alphabet letters by 4 positions.

    Non-letter characters are unchanged. Case is preserved.
    '''
    def _shift_char(c: str, base: int) -> str:
        return chr((ord(c) - base + 4) % 26 + base)

    res = []
    for ch in s:
        if 'a' <= ch <= 'z':
            res.append(_shift_char(ch, ord('a')))
        elif 'A' <= ch <= 'Z':
            res.append(_shift_char(ch, ord('A')))
        else:
            res.append(ch)
    return ''.join(res)


if __name__ == '__main__':
    # quick demo
    print(encrypt('hello, World!'))
