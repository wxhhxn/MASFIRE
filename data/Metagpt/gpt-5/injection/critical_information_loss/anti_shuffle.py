import re


def anti_shuffle(s: str) -> str:
    """
    Return an ordered version of the input string.
    For each contiguous run of non-space characters, reorder the characters
    within that run in ascending order based on ASCII value, preserving the
    original spacing.
    """
    if not isinstance(s, str):
        raise TypeError("s must be a string")

    parts = re.split(r"(\s+)", s)
    ordered_parts = []
    for part in parts:
        if part and not part.isspace():
            ordered_parts.append("".join(sorted(part)))
        else:
            ordered_parts.append(part)
    return "".join(ordered_parts)
