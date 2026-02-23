from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    n = len(grid)
    # Find the position of value N*N
    r = c = -1
    for i in range(n):
        for j in range(n):
            if grid[i][j] == n*n:
                r, c = i, j
                break
        if r != -1:
            break
    res = [n*n]
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1,1),(1,-1),(-1,1),(-1,-1)]
    for _ in range(1, k):
        best_val = -1
        best_r, best_c = r, c
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                v = grid[nr][nc]
                if v > best_val:
                    best_val = v
                    best_r, best_c = nr, nc
        r, c = best_r, best_c
        res.append(grid[r][c])
    return res
