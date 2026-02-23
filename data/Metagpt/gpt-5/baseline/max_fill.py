import math

def max_fill(grid, capacity):
    total = 0
    for row in grid:
        units = sum(row)
        total += math.ceil(units / capacity)
    return total
