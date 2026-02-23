def max_fill(grid, capacity):
    import math
    
    if not grid or not grid[0]:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    
    # Calculate total water in each column (each 1 represents 2 units)
    column_water = [0] * cols
    for j in range(cols):
        for i in range(rows):
            if grid[i][j] == 1:
                column_water[j] += 2
    
    operations = 0
    
    while True:
        # Find column with maximum water
        max_water = max(column_water)
        if max_water <= 0:
            break
        
        max_col = column_water.index(max_water)
        
        # Calculate how much we can extract (minimum of capacity and remaining water)
        extract = min(capacity, column_water[max_col])
        operations += 1
        
        # Apply extraction to target column
        column_water[max_col] -= extract
        
        # Apply overflow to adjacent columns (1 unit each)
        if max_col > 0:
            column_water[max_col - 1] = max(0, column_water[max_col - 1] - 1)
        if max_col < cols - 1:
            column_water[max_col + 1] = max(0, column_water[max_col + 1] - 1)
    
    return operations