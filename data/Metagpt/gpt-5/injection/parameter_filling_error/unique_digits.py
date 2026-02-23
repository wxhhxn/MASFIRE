def unique_digits(x):
    """Return a sorted list of elements from x whose digits are all odd (1, 3, 5, 7, 9)."""
    odd_digits = set('13579')
    filtered = [n for n in x if all(ch in odd_digits for ch in str(n))]
    return sorted(filtered)
