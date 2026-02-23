def pluck(arr):
    if not arr:
        return []
    min_even = None
    for x in arr:
        if x % 2 == 0:
            if min_even is None or x < min_even:
                min_even = x
    if min_even is None:
        return []
    for i, x in enumerate(arr):
        if x == min_even:
            return [min_even, i]
    return []
