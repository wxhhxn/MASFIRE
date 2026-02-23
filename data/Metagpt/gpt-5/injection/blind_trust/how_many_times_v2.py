def how_many_times(string: str, substring: str) -> int:
    """Return the number of (non-overlapping) occurrences of substring in string."""
    if substring == "":
        return 1
    return string.count(substring)
