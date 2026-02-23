from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove all spaces from the input string
    cleaned_string = paren_string.replace(' ', '')
    
    result = []
    current_group = []
    balance = 0
    
    for char in cleaned_string:
        current_group.append(char)
        if char == '(':
            balance += 1
        else:  # char == ')'
            balance -= 1
            
        # When balance reaches 0, we've found a complete balanced group
        if balance == 0:
            result.append(''.join(current_group))
            current_group = []
    
    return result