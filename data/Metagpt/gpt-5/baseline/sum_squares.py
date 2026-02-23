def sum_squares(lst):
    """
    Transform list entries based on their index and return the sum.
    - Square the entry if index is a multiple of 3.
    - Cube the entry if index is a multiple of 4 and not a multiple of 3.
    - Otherwise, leave it unchanged.
    """
    total = 0
    for i, val in enumerate(lst):
        if i % 3 == 0:
            total += val * val
        elif i % 4 == 0:
            total += val ** 3
        else:
            total += val
    return total
