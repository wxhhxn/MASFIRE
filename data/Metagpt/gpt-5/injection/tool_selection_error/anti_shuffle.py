import re


def anti_shuffle(s: str) -> str:
    """
    Return a version of the input string where each non-whitespace chunk
    has its characters sorted in ascending ASCII order, while preserving
    the original whitespace and their positions.
    """
    parts = re.split(r"(\s+)", s)
    return "".join(("".join(sorted(part)) if part and not part.isspace() else part) for part in parts)
