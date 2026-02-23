def sorted_list_sum(lst):
    """Filters even-length strings and sorts by length descending then case-insensitive alphabetical with uppercase first."""
    filtered = [s for s in lst if len(s) % 2 == 0]
    filtered.sort(key=lambda s: (-len(s), s.lower(), [1 if c.isupper() else 0 for c in s]))
    return filtered