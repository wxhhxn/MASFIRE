import re
from typing import List

def words_string(s: str) -> List[str]:
    """
    Split a string of words separated by commas or whitespace into a list of words.

    Delimiters: comma and any whitespace. Multiple separators are collapsed.
    Surrounding whitespace is trimmed and empty tokens are ignored. Order is preserved.
    """
    if not s:
        return []
    tokens = re.split(r"[\s,]+", s.strip())
    return [t for t in tokens if t]
