def minPath(grid, k):
    n = len(grid)
    # Find the position of value 1
    r = c = -1
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                r, c = i, j
                break
        if r != -1:
            break

    # Find the minimal neighbor value of the cell containing 1
    mn = None
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n:
            val = grid[nr][nc]
            if mn is None or val < mn:
                mn = val

    if k == 1:
        return [1]

    # Build the lexicographically smallest path by alternating between 1 and mn
    res = []
    for idx in range(k):
        if idx % 2 == 0:
            res.append(1)
        else:
            res.append(mn)
    return res
