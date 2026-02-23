def separate_paren_groups(paren_string: str) -> list[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those groups into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces and consider only parentheses
    s = ''.join(ch for ch in paren_string if ch != ' ')
    groups: list[str] = []
    balance = 0
    current: list[str] = []

    for ch in s:
        if ch not in ('(', ')'):
            # Ignore any non-parenthesis characters just in case
            continue
        current.append(ch)
        if ch == '(':
            balance += 1
        else:
            balance -= 1
        if balance == 0 and current:
            groups.append(''.join(current))
            current = []

    return groups
