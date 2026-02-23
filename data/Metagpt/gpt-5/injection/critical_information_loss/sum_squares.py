def sum_squares(lst: list[int]) -> int:
    """
    Process a list of integers based on index-dependent rules and return the aggregated sum.

    Rules:
    - If an element's index is a multiple of 3, square the element.
    - If an element's index is a multiple of 4 and not a multiple of 3, cube the element.
    - Otherwise, leave the element unchanged.

    Examples:
    - For lst = [1, 2, 3], the output should be 6
    - For lst = [], the output should be 0
    - For lst = [-1, -5, 2, -1, -5], the output should be -126
    """
    total = 0
    for idx, val in enumerate(lst):
        if idx % 3 == 0:
            total += val * val
        elif idx % 4 == 0:
            total += val * val * val
        else:
            total += val
    return total
