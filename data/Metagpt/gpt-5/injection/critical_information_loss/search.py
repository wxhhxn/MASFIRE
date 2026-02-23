from collections import Counter


def search(lst):
    """
    Return the greatest integer x > 0 such that its frequency in lst is >= x; otherwise -1.
    """
    counts = Counter(lst)
    result = -1
    for x, freq in counts.items():
        if x > 0 and freq >= x and x > result:
            result = x
    return result
