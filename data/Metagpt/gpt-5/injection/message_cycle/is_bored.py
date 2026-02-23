import re

def is_bored(S):
    sentences = re.split(r'[.?!]', S)
    return sum(1 for s in sentences if s.strip() and re.match(r'^\s*I(\b|$)', s))
