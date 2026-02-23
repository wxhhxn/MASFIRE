def pluck(arr):
    best_value = None
    best_index = -1
    for i, x in enumerate(arr):
        if x % 2 == 0:
            if best_value is None or x < best_value:
                best_value = x
                best_index = i
    if best_value is None:
        return []
    return [best_value, best_index]
