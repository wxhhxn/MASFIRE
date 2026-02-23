from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    count_odd_lst1 = sum(1 for x in lst1 if x % 2 == 0)
    count_even_lst2 = sum(1 for x in lst2 if x % 2 == 0)
    return "YES" if count_odd_lst1 >= count_even_lst2 else "NO"
