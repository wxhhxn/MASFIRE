def will_it_fly(q, w):
    if not isinstance(q, list):
        return False
    if q != q[::-1]:
        return False
    try:
        total = sum(q)
    except TypeError:
        return False
    return total <= w
