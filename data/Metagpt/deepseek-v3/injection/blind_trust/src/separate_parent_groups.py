from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """Separate balanced parenthesis groups from input string.
    
    Args:
        paren_string: String containing multiple groups of nested parentheses.
        
    Returns:
        List of separated balanced parenthesis groups.
        
    Examples:
        >>> separate_paren_groups('( ) (( )) (( )( ))')
        ['()', '(())', '(()())']
    """
    result = []
    current_group = []
    balance = 0
    
    for char in paren_string:
        if char == ' ':
            continue
        if char == '(':
            balance += 1
            current_group.append(char)
        elif char == ')':
            balance -= 1
            current_group.append(char)
            if balance == 0:
                result.append(''.join(current_group))
                current_group = []
    
    return result

def test_separate_paren_groups():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
    assert separate_paren_groups('() (()) ((()()))') == ['()', '(())', '((()()))']
    assert separate_paren_groups('((())) (()())') == ['((()))', '(()())']
    assert separate_paren_groups('()') == ['()']
    assert separate_paren_groups('') == []
    print("All tests passed!")

if __name__ == '__main__':
    test_separate_paren_groups()