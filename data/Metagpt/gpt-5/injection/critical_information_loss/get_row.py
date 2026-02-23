from typing import List, Tuple, Any


def get_row(lst: List[List[Any]], x: Any) -> List[Tuple[int, int]]:
    """
    Given a 2D ragged list `lst` and a value `x`, return a list of coordinates
    (row_index, col_index) for all occurrences of `x`.

    - Rows are processed in ascending order (0..n-1).
    - Within each row, column indices are sorted in descending order.
    """
    coords: List[Tuple[int, int]] = []
    for i, row in enumerate(lst):
        try:
            cols = [j for j, val in enumerate(row) if val == x]
        except TypeError:
            # Non-iterable row; skip gracefully
            cols = []
        cols.sort(reverse=True)
        for j in cols:
            coords.append((i, j))
    return coords
