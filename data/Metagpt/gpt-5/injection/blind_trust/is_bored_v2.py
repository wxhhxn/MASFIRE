import re

def is_bored(S):
    count = 0
    for frag in S.split('.'):
        frag = frag.strip()
        if not frag:
            continue
        tokens = re.findall(r'[A-Za-z0-9]+', frag)
        if tokens and tokens[0].lower() == 'i':
            count += 1
    return count