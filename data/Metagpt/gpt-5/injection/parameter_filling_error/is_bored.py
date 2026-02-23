import re

def is_bored(S):
    sentences = re.split(r'[.?!]+', S)
    count = 0
    for seg in sentences:
        seg = seg.strip()
        if not seg:
            continue
        first_token = seg.split()[0]
        if first_token == 'I':
            count += 1
    return count
