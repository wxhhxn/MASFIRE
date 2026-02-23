def is_sorted(lst):
    if len(lst) <= 1:
        return True
    prev = lst[0]
    for x in lst[1:]:
        if x <= prev:
            return False
        prev = x
    return True
