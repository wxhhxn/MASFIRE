from typing import List



def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    groups = paren_string.strip().split()
    depths: List[int] = []
    for grp in groups:
        depth = 0
        max_depth = 0
        for ch in grp:
            if ch == '(':  # entering a new level
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            elif ch == ')':  # leaving a level
                depth -= 1
        depths.append(max_depth)
    return depths
