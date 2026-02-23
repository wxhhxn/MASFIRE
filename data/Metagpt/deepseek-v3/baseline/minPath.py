def minPath(grid, k):
    """
    Given a grid with N rows and N columns (N >= 2) and a positive integer k, 
    each cell of the grid contains a value. Every integer in the range [1, N * N]
    inclusive appears exactly once on the cells of the grid.

    You have to find the minimum path of length k in the grid.
    """
    n = len(grid)
    
    # Find all possible starting positions (cells with smallest values first)
    positions = []
    for i in range(n):
        for j in range(n):
            positions.append((grid[i][j], i, j))
    positions.sort()
    
    # Directions for movement (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    min_path = None
    
    for val, i, j in positions:
        # BFS queue: (current path, current position)
        queue = [([grid[i][j]], (i, j))]
        
        while queue:
            path, (x, y) = queue.pop(0)
            
            if len(path) == k:
                if min_path is None or path < min_path:
                    min_path = path
                # Since positions are sorted by value, first valid path is minimal
                if min_path == path:
                    return min_path
                continue
            
            # Explore all neighboring cells
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    new_path = path + [grid[nx][ny]]
                    queue.append((new_path, (nx, ny)))
    
    return min_path