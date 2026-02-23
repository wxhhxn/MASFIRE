from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    groups = paren_string.split()
    depths: List[int] = []
    for g in groups:
        current_depth = 0
        max_depth = 0
        for ch in g:
            if ch == '(':  # increment on opening parenthesis
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            elif ch == ')':  # decrement on closing parenthesis
                current_depth -= 1
            else:
                continue
        depths.append(max_depth)
    return depths
