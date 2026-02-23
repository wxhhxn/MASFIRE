"""Utilities for filtering positive numbers from lists."""

def get_positive(lst):
    """Return a new list containing only positive numeric values from lst.

    Non-numeric items are ignored. If lst is None, an empty list is returned.
    """
    if lst is None:
        return []

    result = []
    for item in lst:
        # Accept ints and floats only
        if isinstance(item, (int, float)) and item > 0:
            result.append(item)
    return result
