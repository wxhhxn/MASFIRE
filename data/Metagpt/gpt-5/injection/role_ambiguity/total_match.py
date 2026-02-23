def total_match(lst1: list[str], lst2: list[str]) -> list[str]:
    len1 = sum(len(s) for s in lst1)
    len2 = sum(len(s) for s in lst2)
    return lst1 if len1 <= len2 else lst2
