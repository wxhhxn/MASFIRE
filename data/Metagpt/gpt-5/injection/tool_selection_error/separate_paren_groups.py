from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    s = paren_string.replace(" ", "")
    result: List[str] = []
    buffer: List[str] = []
    balance = 0

    for ch in s:
        if ch == "(":
            buffer.append("(")
            balance += 1
        elif ch == ")":
            buffer.append(")")
            balance -= 1
            if balance == 0:
                result.append("".join(buffer))
                buffer = []

    return result
