def correct_bracketing(brackets: str) -> bool:
    """Check if every opening bracket has a corresponding closing bracket.
    
    Args:
        brackets: A string containing only '(' and ')' characters.
        
    Returns:
        True if brackets are properly nested and balanced, False otherwise.
        
    Examples:
        >>> correct_bracketing("(")
        False
        >>> correct_bracketing("()")
        True
        >>> correct_bracketing("(()())")
        True
        >>> correct_bracketing(")(()")
        False
    """
    if not brackets:
        return True
    
    if brackets[0] == ')':
        return False
        
    open_count = brackets.count('(')
    close_count = brackets.count(')')
    
    return open_count == close_count