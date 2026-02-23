def max_fill(grid, capacity):
    import math
    """
    Compute the number of times buckets must be lowered to empty all wells.
    Each row represents one well; each 1 in a row is one unit of water.
    All buckets share the same capacity.
    The total lowerings equal the sum across wells of ceil(units_in_well / capacity).
    """
    return sum(math.ceil(sum(row) / capacity) for row in grid)
