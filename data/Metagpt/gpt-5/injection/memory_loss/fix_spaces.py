import re


def fix_spaces(text: str) -> str:
    """
    Replace runs of 3 or more consecutive spaces with a single '-' character,
    then replace remaining spaces (single or double) with underscores '_'.
    Non-space characters remain unchanged.
    """
    # Replace sequences of 3 or more spaces with a single '-'
    result = re.sub(r" {3,}", "-", text)
    # Replace remaining spaces (1 or 2 in a run) with underscores, one per space
    return result.replace(" ", "_")
