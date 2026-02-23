from typing import List, Tuple, Any

def get_row(lst: List[List[Any]], x: Any) -> List[Tuple[int, int]]:
    """
    Return coordinates (row, col) for occurrences of x in a ragged 2D list.
    Rows are processed in ascending order (0-based). Within each row, matching
    column indices are sorted in descending order.
    """
    result: List[Tuple[int, int]] = []
    for r, row in enumerate(lst):
        cols = [c for c, val in enumerate(row) if val == x]
        for c in sorted(cols, reverse=True):
            result.append((r, c))
    return result
