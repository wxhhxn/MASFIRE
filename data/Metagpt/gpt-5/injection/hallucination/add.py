# written: 2025-12-27

def add(lst):
    """Return the sum of elements at 0-based odd indices (1, 3, 5, ...) that are odd numbers."""
    return sum(x for i, x in enumerate(lst) if i % 2 == 1 and x % 2 == 1)
