from typing import Any, List, Tuple


def get_row(lst: List[List[Any]], x: Any) -> List[Tuple[int, int]]:
    """
    Return coordinates (row, column) where elements equal x in a ragged 2D list.
    Rows are emitted in ascending order; within each row, columns are in descending order.
    """
    result: List[Tuple[int, int]] = []
    for i, row in enumerate(lst):
        matching_cols = [j for j, val in enumerate(row) if val == x]
        matching_cols.sort(reverse=True)
        result.extend((i, j) for j in matching_cols)
    return result
