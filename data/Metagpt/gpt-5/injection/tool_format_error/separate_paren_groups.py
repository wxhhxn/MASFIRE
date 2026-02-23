from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """Given a string containing multiple balanced groups of parentheses (groups are not nested within each other at the top level), ignore spaces and return a list of the separate groups.
    Example: separate_paren_groups('( ) (( )) (( )( ))') -> ['()', '(())', '(()())']"""
    groups: List[str] = []
    current = []
    balance = 0
    for ch in paren_string:
        if ch == ' ':
            continue
        if ch == '(':
            balance += 1
            current.append('(')
        elif ch == ')':
            balance -= 1
            current.append(')')
        else:
            continue
        if balance == 0 and current:
            groups.append(''.join(current))
            current = []
    return groups
