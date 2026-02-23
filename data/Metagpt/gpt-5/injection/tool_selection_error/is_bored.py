import re

def is_bored(S: str) -> int:
    sentences = re.split(r"[.!?]+", S)
    count = 0
    for s in sentences:
        t = s.strip()
        if not t:
            continue
        if t == "I" or t.startswith("I "):
            count += 1
    return count
