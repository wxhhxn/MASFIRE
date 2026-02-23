import re

def fix_spaces(text: str) -> str:
    """
    Replace single spaces with underscores (_), exactly two spaces with double underscores (__),
    and any run of three or more spaces with a single hyphen (-).
    """
    text = re.sub(r" {3,}", "-", text)
    text = text.replace("  ", "__")
    text = text.replace(" ", "_")
    return text
