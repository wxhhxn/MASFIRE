from typing import List, Tuple


def get_row(lst: List[List[int]], x: int) -> List[Tuple[int, int]]:
    coords: List[Tuple[int, int]] = []
    for i, row in enumerate(lst):
        cols = [j for j, val in enumerate(row) if val == x]
        cols.sort(reverse=True)
        for j in cols:
            coords.append((i, j))
    return coords
