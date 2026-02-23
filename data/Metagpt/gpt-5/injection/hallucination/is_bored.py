import re


def is_bored(S: str) -> int:
    if not S:
        return 0
    sentences = re.split(r"[.!?]+", S)
    count = 0
    for s in sentences:
        s = s.strip()
        if not s:
            continue
        if re.match(r"^I\b", s):
            count += 1
    return count
