from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """Parse groups of nested parentheses and return max nesting depth for each group.
    
    Args:
        paren_string: String containing multiple parenthesis groups separated by spaces.
        
    Returns:
        List of integers representing max nesting depth for each group.
        
    Examples:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
        >>> parse_nested_parens('() () ()')
        [1, 1, 1]
        >>> parse_nested_parens('((()))')
        [3]
        >>> parse_nested_parens('')
        []
    """
    if not paren_string.strip():
        return []
    
    groups = paren_string.split()
    result = []
    
    for group in groups:
        max_depth = current_depth = 0
        for char in group:
            if char == '(':
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            elif char == ')':
                current_depth -= 1
        result.append(max_depth)
    
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    # Additional test cases
    test_cases = [
        ('(()()) ((())) () ((())()())', [2, 3, 1, 3]),
        ('()', [1]),
        ('', []),
        ('((()()))', [3]),
        ('(()) () (()())', [2, 1, 2])
    ]
    
    for input_str, expected in test_cases:
        result = parse_nested_parens(input_str)
        assert result == expected, f"Failed for {input_str}. Expected {expected}, got {result}"
    print("All tests passed!")