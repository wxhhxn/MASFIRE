import math

def max_fill(grid, capacity):
    total_lowerings = 0
    for row in grid:
        ones = sum(row)
        if ones > 0:
            total_lowerings += math.ceil(ones / capacity)
    return total_lowerings
