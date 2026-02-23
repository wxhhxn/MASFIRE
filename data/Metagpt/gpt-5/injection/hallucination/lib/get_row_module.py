def get_row(lst, x):
    """
    Return coordinates of occurrences of x in a nested list using 1-based indexing.
    Rows are processed in descending order; within each row, columns are sorted in ascending order.
    The result is a list of (row, column) tuples.
    """
    result = []
    if not isinstance(lst, list):
        return result
    for r in range(len(lst) - 1, -1, -1):
        row = lst[r]
        if not isinstance(row, list):
            continue
        cols = [c + 1 for c, val in enumerate(row) if val == x]
        if cols:
            cols.sort()
            for c in cols:
                result.append((r + 1, c))
    return result
