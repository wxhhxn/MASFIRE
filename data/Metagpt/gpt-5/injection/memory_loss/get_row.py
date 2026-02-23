from typing import List, Tuple


def get_row(lst: List[List[int]], x: int) -> List[Tuple[int, int]]:
    """
    Given a ragged 2D list of integers and an integer x, return a list of (row, column)
    coordinates where x occurs. Rows are ordered ascending; within each row, columns
    are ordered descending.

    Example:
    >>> get_row([[1,2,3,4,5,6],[1,2,3,4,1,6],[1,2,3,4,5,1]], 1)
    [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    """
    result: List[Tuple[int, int]] = []
    for i, row in enumerate(lst):
        # iterate columns from right to left to satisfy per-row descending order
        for j in range(len(row) - 1, -1, -1):
            if row[j] == x:
                result.append((i, j))
    return result
