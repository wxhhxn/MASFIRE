def by_length(arr):
    """
    Keep only integers in [1..9] from the input array, sort ascending, reverse to descending,
    then map to their corresponding English names.
    """
    names = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    filtered = [x for x in arr if isinstance(x, int) and 1 <= x <= 9]
    filtered.sort()  # ascending
    filtered.reverse()  # descending
    return [names[x] for x in filtered]
