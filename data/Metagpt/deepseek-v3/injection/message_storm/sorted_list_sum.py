def sorted_list_sum(lst):
    # Filter out strings with odd lengths
    filtered_list = [word for word in lst if len(word) % 2 == 0]
    
    # Sort the filtered list: first by length (ascending), then alphabetically
    sorted_list = sorted(filtered_list, key=lambda x: (len(x), x))
    
    return sorted_list