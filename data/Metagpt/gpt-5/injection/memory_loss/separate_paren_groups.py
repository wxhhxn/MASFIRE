from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """Separate balanced, non-nested parenthesis groups from the input string.
    Spaces are ignored.

    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    s = ''.join(ch for ch in paren_string if ch in '()')
    groups: List[str] = []
    depth = 0
    current: List[str] = []

    for ch in s:
        if ch == '(':
            depth += 1
            current.append(ch)
        elif ch == ')':
            current.append(ch)
            depth -= 1
            if depth == 0:
                groups.append(''.join(current))
                current = []

    return groups
