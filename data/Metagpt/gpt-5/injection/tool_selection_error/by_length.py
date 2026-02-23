def by_length(arr):
    """
    Given an array of integers, keep only those between 1 and 9 inclusive,
    sort ascending, reverse to descending, and map digits to their names.
    """
    names = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    filtered = [x for x in arr if isinstance(x, int) and not isinstance(x, bool) and 1 <= x <= 9]
    filtered.sort()
    filtered.reverse()
    return [names[x] for x in filtered]
