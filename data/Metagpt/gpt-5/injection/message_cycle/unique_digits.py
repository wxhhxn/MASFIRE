def unique_digits(x):
    """Return a sorted list of integers from x that contain no even digits."""
    return sorted(n for n in x if all(int(d) % 2 == 1 for d in str(n)))
