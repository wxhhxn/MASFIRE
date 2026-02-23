import re


def is_bored(S: str) -> int:
    """
    Count the number of sentences that start with the word "I".

    Sentences are delimited by '.', '?' or '!'.
    A sentence is considered starting with 'I' if, after trimming leading whitespace
    and common leading punctuation (quotes or brackets), the first word is exactly 'I'.
    """
    if not S:
        return 0
    parts = re.split(r"[.?!]", S)
    count = 0
    for part in parts:
        s = part.strip()
        if not s:
            continue
        # Remove leading quotes/brackets/parentheses and typographic quotes
        s = re.sub(r"^[\s\"'“”‘’\(\[\{]+", "", s)
        if re.match(r"^I\b", s):
            count += 1
    return count
