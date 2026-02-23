from typing import List


def minPath(grid: List[List[int]], k: int) -> List[int]:
    """
    Return the ordered list of values along a lexicographically minimal path of length k on an N x N grid.
    The path starts at the cell with value 1. At each step, move to the in-bounds neighbor (up/down/left/right)
    with the smallest value. You cannot stay in place; revisiting cells is allowed.
    """
    n = len(grid)
    if k <= 0:
        return []

    # Find the position of value 1 to start.
    start_i = start_j = -1
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                start_i, start_j = i, j
                break
        if start_i != -1:
            break

    # Fallback: if 1 is not found (should not happen with valid input), start at global minimum.
    if start_i == -1:
        min_val = grid[0][0]
        start_i, start_j = 0, 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] < min_val:
                    min_val = grid[i][j]
                    start_i, start_j = i, j

    path = [grid[start_i][start_j]]
    if k == 1:
        return path

    i, j = start_i, start_j
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for _ in range(k - 1):
        best_val = None
        best_pos = None
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                val = grid[ni][nj]
                if best_val is None or val < best_val:
                    best_val = val
                    best_pos = (ni, nj)
        # Move to the neighbor with the smallest value.
        i, j = best_pos  # type: ignore
        path.append(best_val)  # type: ignore

    return path
