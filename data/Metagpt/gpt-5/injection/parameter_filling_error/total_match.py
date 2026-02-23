def total_match(lst1, lst2):
    """
    Return the list with smaller total character count across its strings.
    If both have the same total, return the first list.
    """
    sum1 = sum(len(s) for s in lst1)
    sum2 = sum(len(s) for s in lst2)
    return lst1 if sum1 <= sum2 else lst2
