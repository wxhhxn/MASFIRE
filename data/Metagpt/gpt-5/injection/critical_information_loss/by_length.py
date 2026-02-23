def by_length(arr):
    """
    Given an array of integers, keep only those between 1 and 9 inclusive,
    sort them ascending, reverse to descending, and map each to its English name.

    Returns an empty list if input is empty or no valid numbers remain.
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

    # Filter only integer values in [1, 9]
    valid = [x for x in arr if isinstance(x, int) and not isinstance(x, bool) and 1 <= x <= 9]
    if not valid:
        return []

    valid.sort()
    valid.reverse()
    return [names[n] for n in valid]
