from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """Input to this function is a string represented multiple groups for nested parentheses separated by commas.
    For each of the group, output the deepest level of nesting of parentheses. Note: depth counting starts at 0 (so () -> 0).
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [3, 2, 0, 4]
    """
    result = []
    current_max = 0
    current_depth = 0
    
    for group in paren_string.split():
        current_max = 0
        current_depth = 0
        for char in group:
            if char == '(':
                current_depth += 1
                if current_depth > current_max:
                    current_max = current_depth
            elif char == ')':
                current_depth -= 1
        result.append(current_max - 1)  # Subtract 1 to make depth start at 0 for ()
    
    return result

if __name__ == "__main__":
    test_cases = [
        ('(()()) ((())) () ((())()())', [3, 2, 0, 4]),
        ('()', [0]),
        ('(())', [1]),
        ('((()))', [2]),
        ('() () ()', [0, 0, 0]),
    ]
    
    for test_input, expected in test_cases:
        result = parse_nested_parens(test_input)
        assert result == expected, f"Test failed for input '{test_input}'. Expected {expected}, got {result}"
    print("All tests passed!")