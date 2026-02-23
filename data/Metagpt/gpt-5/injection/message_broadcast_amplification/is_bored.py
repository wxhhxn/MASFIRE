import re


def is_bored(S: str) -> int:
    """Count how many sentences start with 'I' (capital I).

    Sentences are delimited by '.', '?' or '!'.
    """
    if not S:
        return 0
    count = 0
    for segment in re.split(r"[.!?]", S):
        s = segment.strip()
        if not s:
            continue
        if re.match(r"^I\b", s):
            count += 1
    return count
