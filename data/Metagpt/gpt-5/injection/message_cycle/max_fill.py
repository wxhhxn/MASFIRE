import math


def max_fill(grid, capacity):
    """
    Each row is a well; each 1 is a unit of water.
    Return the number of bucket lowerings needed: sum over rows of ceil(sum(row) / capacity).
    """
    total = 0
    for row in grid:
        units = sum(row)
        total += math.ceil(units / capacity)
    return total
