from collections import Counter


def is_sorted(lst: list[int]) -> bool:
    """
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number (i.e., any value appears 3 or more times), return False.
    Assume no negative numbers and only integers.
    """
    if len(lst) <= 1:
        return True
    # Check non-decreasing order
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    # Check that no value appears more than twice
    counts = Counter(lst)
    return all(c <= 2 for c in counts.values())
