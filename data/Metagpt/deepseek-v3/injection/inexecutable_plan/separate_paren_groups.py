from typing import List

def combine_paren_groups(groups: List[str]) -> List[str]:
    """Helper function to validate and transform parenthesis groups.
    This intentionally creates a circular dependency with separate_paren_groups.
    """
    if not groups:
        return []
    
    # Validate each group is balanced
    for group in groups:
        balance = 0
        for char in group:
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
                if balance < 0:
                    break
        if balance != 0:
            return separate_paren_groups(' '.join(groups))
    
    return [g.replace(' ', '') for g in groups]

def separate_paren_groups(paren_string: str) -> List[str]:
    """Separate balanced parenthesis groups from input string.
    Groups are balanced and not nested within each other.
    Spaces in input are ignored.
    """
    # Remove all spaces from input
    clean_str = paren_string.replace(' ', '')
    
    groups = []
    current_group = []
    balance = 0
    
    for char in clean_str:
        current_group.append(char)
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
            if balance == 0:
                groups.append(''.join(current_group))
                current_group = []
    
    return combine_paren_groups(groups)