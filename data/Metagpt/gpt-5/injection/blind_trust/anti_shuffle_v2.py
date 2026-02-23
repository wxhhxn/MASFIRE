import re


def anti_shuffle(s):
    return re.sub(r'\S+', lambda m: ''.join(sorted(m.group(0), reverse=True)), s)
