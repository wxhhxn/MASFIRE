import re

def is_bored(S):
    count = 0
    for part in re.split(r'[.?!]', S):
        s = part.strip()
        if not s:
            continue
        first = s.split()[0]
        if first == 'I':
            count += 1
    return count
