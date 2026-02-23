import re


def fix_spaces(text: str) -> str:
    """
    Replace all spaces with underscores, and replace any run of more than
    two consecutive spaces with a single '-'.

    Examples:
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    # Replace runs of 3 or more spaces with a single hyphen
    s = re.sub(r" {3,}", "-", text)
    # Replace remaining spaces with underscores
    return s.replace(" ", "_")
