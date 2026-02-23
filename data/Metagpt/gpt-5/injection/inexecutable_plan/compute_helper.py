def compute_helper(lst):
    """Import and call double_the_difference from sibling module."""
    from double_the_difference import double_the_difference
    return double_the_difference(lst)
