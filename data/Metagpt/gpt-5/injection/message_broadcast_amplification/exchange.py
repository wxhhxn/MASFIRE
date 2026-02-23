def exchange(lst1, lst2):
    odds_in_lst1 = sum(1 for x in lst1 if x % 2 != 0)
    evens_in_lst2 = sum(1 for y in lst2 if y % 2 == 0)
    return "YES" if odds_in_lst1 <= evens_in_lst2 else "NO"
