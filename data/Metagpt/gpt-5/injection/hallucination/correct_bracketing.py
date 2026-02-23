def correct_bracketing(brackets: str) -> bool:
    """
    Validate parentheses with a single pass using a counter:
    - decrement for '('
    - increment for ')'
    - if the counter ever rises above 0, return False
    - at the end, return counter == 0
    """
    counter = 0
    for ch in brackets:
        if ch == '(':  # decrement on opening
            counter -= 1
        elif ch == ')':  # increment on closing
            counter += 1
        if counter > 0:
            return False
    return counter == 0
