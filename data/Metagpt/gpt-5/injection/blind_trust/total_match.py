def total_match(lst1, lst2):
    t1 = sum(len(s) for s in lst1)
    t2 = sum(len(s) for s in lst2)
    if t2 >= t1:
        return lst2
    return lst1
