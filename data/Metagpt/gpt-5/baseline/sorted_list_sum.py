def sorted_list_sum(lst):
    """
    Accepts a list of strings; removes strings with odd lengths; returns the list
    sorted ascending by length and alphabetically for equal lengths. Duplicates
    are preserved.
    """
    filtered = [s for s in lst if isinstance(s, str) and len(s) % 2 == 0]
    return sorted(filtered, key=lambda s: (len(s), s))
