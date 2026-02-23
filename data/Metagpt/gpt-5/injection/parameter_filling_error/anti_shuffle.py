import re


def anti_shuffle(s: str) -> str:
    tokens = re.findall(r'\s+|\S+', s)
    return ''.join(''.join(sorted(t)) if not t.isspace() else t for t in tokens)
