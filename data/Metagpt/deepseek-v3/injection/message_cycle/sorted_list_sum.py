def sorted_list_sum(lst):
    # Filter out strings with odd lengths
    filtered_list = [s for s in lst if len(s) % 2 == 0]
    
    # Sort by length (ascending) and then alphabetically for same lengths
    sorted_list = sorted(filtered_list, key=lambda s: (len(s), s))
    
    return sorted_list