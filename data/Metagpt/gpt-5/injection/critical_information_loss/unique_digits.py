def unique_digits(x):
    """Given a list of positive integers x, return a sorted list of all elements that haven't any even digit."""
    return sorted([n for n in x if all(int(d) % 2 == 1 for d in str(n))])
