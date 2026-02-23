from collections import Counter


def is_sorted(lst):
    """Return True if lst of non-negative integers is non-decreasing and no element appears more than twice.

    Conditions:
    - Non-decreasing order (each element >= previous element)
    - No value appears more than twice (frequency > 2 -> False)
    """
    # Check non-decreasing order
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return False

    # Check frequency constraint: no value appears more than twice
    counts = Counter(lst)
    if any(c > 2 for c in counts.values()):
        return False

    return True
