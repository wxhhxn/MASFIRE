def get_row(lst, x):
    """
    Return a list of (row_index, col_index) tuples where x occurs in lst (a jagged 2D list).
    Rows are ordered ascending by row index, and within each row, columns are ordered descending.
    """
    coords = []
    for i, row in enumerate(lst):
        cols = [j for j, val in enumerate(row) if val == x]
        if cols:
            for j in sorted(cols, reverse=True):
                coords.append((i, j))
    return coords
