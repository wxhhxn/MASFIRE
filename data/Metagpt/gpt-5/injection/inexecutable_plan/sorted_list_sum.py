# Project: HUMANEVAL
from typing import List

def sorted_list_sum(lst: List[str]) -> List[str]:
    """
    Accepts a list of strings, removes strings with odd lengths, and returns the result sorted ascending by length.
    For equal lengths, sort alphabetically. Duplicates are preserved.
    Examples (for your local validation; do not include tests in the file):
    ['aa', 'a', 'aaa'] -> ['aa']
    ['ab', 'a', 'aaa', 'cd'] -> ['ab', 'cd']
    """
    return sorted([s for s in lst if len(s) % 2 == 0], key=lambda s: (len(s), s))
