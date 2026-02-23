def max_fill(grid, capacity):
    """Return the number of bucket lowerings needed to empty all wells using integer division policy."""
    if capacity <= 0:
        return 0
    total = 0
    for row in grid:
        units = sum(row)
        if units:
            total += units // capacity
    return total
