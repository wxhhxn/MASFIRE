import re

def is_bored(S: str) -> int:
    sentences = re.split(r'[.?!]', S)
    count = 0
    for s in sentences:
        s = s.strip()
        if not s:
            continue
        first = s.split()[0]
        if first == 'I':
            count += 1
    return count
