import re


def is_bored(S: str) -> int:
    """
    Count how many sentences in S start with the exact uppercase word "I".
    Sentences are delimited by '.', '?' or '!'. Leading spaces before the
    first character of a sentence are ignored. Contractions like "I'm"
    are NOT counted.
    """
    parts = re.split(r'[.?!]', S)
    count = 0
    for part in parts:
        s = part.lstrip()
        if not s:
            continue
        if s[0] == 'I':
            if len(s) == 1:
                count += 1
            else:
                nxt = s[1]
                # Count only if next char is not a letter and not an apostrophe
                if not nxt.isalpha() and nxt != "'":
                    count += 1
    return count
