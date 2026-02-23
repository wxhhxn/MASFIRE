import re


def fix_spaces(text: str) -> str:
    """
    Normalize spacing in a string:
    - Replace single spaces with underscores.
    - Replace any run of 3 or more consecutive spaces with a single dash ('-').

    Examples:
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    # Replace runs of 3+ spaces with a single '-'
    s = re.sub(r" {3,}", "-", text)
    # Replace remaining spaces (single or double) with underscores
    return s.replace(" ", "_")
