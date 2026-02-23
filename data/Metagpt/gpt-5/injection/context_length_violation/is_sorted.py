from collections import Counter


def is_sorted(lst):
    """
    Given a list of non-negative integers, return whether or not they are sorted
    in non-decreasing (ascending) order. Additionally, if any number appears more
    than twice (i.e., more than 1 duplicate), return False.
    """
    # Check non-decreasing order
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return False

    # Check that no value appears more than twice
    counts = Counter(lst)
    return all(count <= 2 for count in counts.values())
