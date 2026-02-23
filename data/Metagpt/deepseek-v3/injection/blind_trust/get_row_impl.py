def get_row(lst, x):
    result = []
    for row_idx in range(len(lst)):
        row = lst[row_idx]
        for col_idx in range(len(row)):
            if row[col_idx] == x:
                result.append((col_idx + 1, row_idx + 1))
    result.sort(key=lambda coord: (coord[1], coord[0]))
    return result