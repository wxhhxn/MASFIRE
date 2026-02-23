from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """Separate balanced, non-overlapping groups of parentheses from a string.
    Spaces in the input are ignored.

    Example:
        >>> separate_paren_groups('( ) (( )) (( )( ))')
        ['()', '(())', '(()())']
    """
    groups: List[str] = []
    current: List[str] = []
    balance = 0

    for ch in paren_string:
        if ch == ' ':
            continue
        if ch == '(':
            balance += 1
            current.append(ch)
        elif ch == ')':
            balance -= 1
            current.append(ch)
        else:
            # Ignore any non-parenthesis characters
            continue

        if balance == 0 and current:
            groups.append(''.join(current))
            current = []

    return groups
