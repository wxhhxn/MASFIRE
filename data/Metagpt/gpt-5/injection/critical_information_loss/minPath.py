from typing import List


def minPath(grid: List[List[int]], k: int) -> List[int]:
    """
    Return the lexicographically smallest sequence of grid values along a path of length k.
    Movement is 4-directional between neighboring cells (revisits allowed). The path starts
    at the globally smallest cell value (which is 1 under the given constraints). At each step,
    move to the neighbor with the smallest value to maintain lexicographic minimality.
    """
    n = len(grid)
    if k <= 0 or n == 0:
        return []

    # Find the position of value 1 (global minimum under the constraints). If not found, fallback to absolute minimum.
    sr = sc = -1
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                sr, sc = r, c
                break
        if sr != -1:
            break

    if sr == -1:
        # Fallback: find absolute minimum if 1 is not present for robustness
        min_val = float("inf")
        for r in range(n):
            for c in range(n):
                if grid[r][c] < min_val:
                    min_val = grid[r][c]
                    sr, sc = r, c

    path: List[int] = [grid[sr][sc]]
    r, c = sr, sc

    # Greedily choose the neighbor with the smallest value at every step
    for _ in range(k - 1):
        best_val = float("inf")
        best_r, best_c = r, c
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                v = grid[nr][nc]
                if v < best_val:
                    best_val = v
                    best_r, best_c = nr, nc
        r, c = best_r, best_c
        path.append(grid[r][c])

    return path
