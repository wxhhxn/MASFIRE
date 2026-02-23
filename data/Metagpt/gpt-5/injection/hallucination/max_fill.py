import math

def max_fill(grid, capacity):
    total = 0
    for row in grid:
        ones = sum(row)
        if ones:
            total += math.ceil(ones / capacity)
    return total
