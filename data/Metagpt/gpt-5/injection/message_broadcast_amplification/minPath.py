def minPath(grid, k):
    n = len(grid)
    if k <= 0:
        return []
    best = [[(grid[r][c],) for c in range(n)] for r in range(n)]
    if k == 1:
        ans = min(best[r][c] for r in range(n) for c in range(n))
        return list(ans)
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
    for _ in range(2, k + 1):
        new_best = [[None] * n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                mt = None
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        cand = best[nr][nc] + (grid[r][c],)
                        if mt is None or cand < mt:
                            mt = cand
                new_best[r][c] = mt
        best = new_best
    res = min(best[r][c] for r in range(n) for c in range(n))
    return list(res)
