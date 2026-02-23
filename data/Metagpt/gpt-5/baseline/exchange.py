def exchange(lst1, lst2):
    """
    Determine if elements can be exchanged between lst1 and lst2 to make all elements of lst1 even.
    Return "YES" if possible, otherwise "NO".
    """
    count_odd_in_lst1 = sum((x % 2) != 0 for x in lst1)
    count_even_in_lst2 = sum((x % 2) == 0 for x in lst2)
    return "YES" if count_even_in_lst2 >= count_odd_in_lst1 else "NO"
