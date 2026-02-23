from __future__ import unicode_literals

def flip_case(s):
    result = []
    for c in s:
        if c.isalpha():
            result.append(chr(ord(c) ^ 32))
        else:
            result.append(c)
    return ''.join(result)