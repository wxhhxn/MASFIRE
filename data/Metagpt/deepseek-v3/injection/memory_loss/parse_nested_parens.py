from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    result = []
    current_max = 0
    current_level = 0
    
    for group in paren_string.split():
        current_max = 0
        current_level = 0
        for char in group:
            if char == '(':
                current_level += 1
                if current_level > current_max:
                    current_max = current_level
            elif char == ')':
                current_level -= 1
        result.append(current_max)
    
    return result