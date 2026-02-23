def match_parens(lst):
    """
    Checks if two parenthesis strings can be concatenated to form a balanced string.
    
    Args:
        lst: A list of two strings containing only '(' and ')'
        
    Returns:
        bool: True if the strings can form a balanced string when concatenated in some order,
              False otherwise.
    """
    s1, s2 = lst
    
    # Check total counts of parentheses
    total_open = s1.count('(') + s2.count('(')
    total_close = s1.count(')') + s2.count(')')
    
    # For balanced parentheses, counts must be equal
    if total_open != total_close:
        return False
        
    # Check if either string has more closing than opening parentheses
    def is_valid(s):
        balance = 0
        for char in s:
            if char == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return True
    
    # Try both concatenation orders
    return is_valid(s1 + s2) or is_valid(s2 + s1)