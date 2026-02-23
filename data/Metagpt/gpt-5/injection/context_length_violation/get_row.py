def get_row(lst, x):
    """
    Given a 2D ragged list `lst` and an integer `x`, find all coordinates
    (row, column) where `x` occurs.
    - Rows are 0-indexed.
    - Return coordinates sorted by rows in ascending order.
    - For each row, sort columns in descending order.

    Examples:
    >>> get_row([[1,2,3,4,5,6],[1,2,3,4,1,6],[1,2,3,4,5,1]], 1)
    [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    >>> get_row([], 1)
    []
    >>> get_row([[], [1], [1, 2, 3]], 3)
    [(2, 2)]
    """
    result = []
    for i, row in enumerate(lst):
        cols = [j for j, val in enumerate(row) if val == x]
        cols.sort(reverse=True)
        for j in cols:
            result.append((i, j))
    return result
