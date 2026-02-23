def is_sorted(lst):
    if not lst:
        return True
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            return False
    counts = {}
    for num in lst:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > 2:
            return False
    return True