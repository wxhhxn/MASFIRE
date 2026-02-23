def correct_bracketing(brackets: str) -> bool:
    """
    Return True if the input string of parentheses is balanced.

    A balanced string never closes more parentheses than have been opened
    at any point, and ends with all opens closed.

    Args:
        brackets: A string consisting only of '(' and ')'.

    Returns:
        bool: True if balanced, False otherwise.
    """
    count = 0
    for ch in brackets:
        if ch == '(':  # opening parenthesis
            count += 1
        elif ch == ')':  # closing parenthesis
            if count == 0:
                return False
            count -= 1
        else:
            # Invalid character for robustness
            return False
    return count == 0
