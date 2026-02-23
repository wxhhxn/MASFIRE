def sort_third(l: list):
    from list_utils import indices_divisible_by_three
    from config.sorting import THIRD_SORT_KEY
    
    indices_to_sort = indices_divisible_by_three(l)
    values_to_sort = [l[i] for i in indices_to_sort]
    values_to_sort.sort(key=THIRD_SORT_KEY)
    
    result = l.copy()
    for i, val in zip(indices_to_sort, values_to_sort):
        result[i] = val
    
    return result