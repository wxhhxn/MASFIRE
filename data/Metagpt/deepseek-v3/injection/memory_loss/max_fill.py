import math

def max_fill(grid, capacity):
    """
    Calculate the number of bucket operations needed to empty all wells.

    Args:
        grid: A 2D list representing wells, where 1 represents water unit
        capacity: The capacity of each bucket

    Returns:
        int: Total number of bucket operations needed

    Examples:
        >>> max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1)
        6
        >>> max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2)
        5
        >>> max_fill([[0,0,0], [0,0,0]], 5)
        0
    """
    if not grid or capacity <= 0:
        return 0
    
    total_operations = 0
    
    for well in grid:
        water_units = sum(well)
        if water_units > 0:
            operations = math.ceil(water_units / capacity)
            total_operations += operations
    
    return total_operations