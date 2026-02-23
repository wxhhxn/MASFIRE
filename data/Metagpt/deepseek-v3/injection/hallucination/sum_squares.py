import math

def sum_squares(lst):
    """
    Processes a list of integers according to index-based rules and returns their sum.
    1. Cubes elements at indexes that are multiples of 3 (1-based)
    2. Squares elements at indexes that are multiples of 4 but not 3 (1-based)
    3. Leaves other elements unchanged
    4. Returns the sum of all processed elements
    
    Args:
        lst: List of integers to process
        
    Returns:
        Sum of processed elements
    """
    total = 0
    for i in range(len(lst)):
        index = i + 1  # Convert to 1-based indexing
        value = lst[i]
        
        if index % 3 == 0:
            # Cube if index is multiple of 3
            processed = math.pow(value, 3)
        elif index % 4 == 0 and index % 3 != 0:
            # Square if index is multiple of 4 but not 3
            processed = math.pow(value, 2)
        else:
            # Leave unchanged otherwise
            processed = value
            
        total += processed
        
    return int(total) if total.is_integer() else total