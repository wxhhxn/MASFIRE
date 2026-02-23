from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces to treat groups as contiguous sequences of parentheses
    s = ''.join(c for c in paren_string if c != ' ')
    result: List[str] = []
    balance = 0
    current: list[str] = []

    for c in s:
        if c not in ('(', ')'):
            # Skip any non-parenthesis characters just in case
            continue
        current.append(c)
        if c == '(':
            balance += 1
        else:
            balance -= 1
        if balance == 0 and current:
            result.append(''.join(current))
            current = []

    return result
