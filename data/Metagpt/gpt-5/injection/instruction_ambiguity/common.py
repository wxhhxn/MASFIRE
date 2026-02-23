def common(l1: list, l2: list):
    """
    Return the unique shared items for two groups, sorted ascending.
    Assumes elements are hashable and mutually comparable.
    """
    return sorted(set(l1) & set(l2))