def is_sorted(lst):
    """Return True if `lst` is sorted in non-decreasing order and
    no number appears more than twice (i.e., at most one duplicate).

    Examples:
        is_sorted([]) -> True
        is_sorted([1, 1, 2]) -> True
        is_sorted([1, 1, 1]) -> False
        is_sorted([1, 3, 2]) -> False
    """
    if not lst:
        return True

    prev = lst[0]
    counts = {prev: 1}

    for x in lst[1:]:
        # Must be non-decreasing
        if x < prev:
            return False
        # Track occurrences and ensure no more than 2
        counts[x] = counts.get(x, 0) + 1
        if counts[x] > 2:
            return False
        prev = x

    return True
