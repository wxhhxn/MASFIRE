from typing import List, Tuple, Any


def get_row(lst: List[List[Any]], x: Any) -> List[Tuple[int, int]]:
    coords: List[Tuple[int, int]] = []
    for i, row in enumerate(lst):
        for j, val in enumerate(row):
            if val == x:
                coords.append((i, j))
    coords.sort(key=lambda t: (t[0], -t[1]))
    return coords
