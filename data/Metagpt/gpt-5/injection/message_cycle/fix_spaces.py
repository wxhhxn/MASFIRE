import re


def fix_spaces(text: str) -> str:
    return re.sub(r' {3,}', '-', text).replace(' ', '_')
