from typing import List, Tuple


def get_row(lst: List[List[int]], x: int) -> List[Tuple[int, int]]:
    """
    Return coordinates (row, column) of occurrences of x in a ragged 2D list.
    Rows are processed in ascending order; within each row,
    matching column indices are added in descending order.
    """
    result: List[Tuple[int, int]] = []
    for i, row in enumerate(lst):
        if not row:
            continue
        cols = [j for j, val in enumerate(row) if val == x]
        if cols:
            cols.sort(reverse=True)
            result.extend((i, j) for j in cols)
    return result
