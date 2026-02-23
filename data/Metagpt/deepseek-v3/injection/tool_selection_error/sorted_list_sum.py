def sorted_list_sum(lst):
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order.
    """
    filtered = [word for word in lst if len(word) % 2 == 0]
    return sorted(filtered, key=lambda x: (len(x), x))