import math

def max_fill(grid, capacity):
    """
    Calculate the number of times buckets need to be lowered to empty wells.

    Args:
        grid: A rectangular grid of wells where each 1 represents a unit of water.
        capacity: The capacity of each bucket (all buckets have same capacity).

    Returns:
        int: The total number of bucket operations needed to empty all wells.

    Examples:
        >>> max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1)
        6
        >>> max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2)
        5
        >>> max_fill([[0,0,0], [0,0,0]], 5)
        0
    """
    total_operations = 0
    
    for well in grid:
        water_units = sum(well)
        if water_units > 0:
            operations = math.ceil(water_units / capacity)
            total_operations += operations
    
    return total_operations