def largest_smallest_integers(lst):
    """
    Return a tuple (a, b):
    - a: the most negative integer from lst (largest negative by absolute value).
    - b: the largest non-negative integer from lst (0 is considered positive).
    Non-numeric items are ignored. Floats are truncated toward zero.
    If no negative or no non-negative integers exist, return None for that value.
    """
    negatives = []
    positives = []
    for x in lst:
        if isinstance(x, bool) or isinstance(x, (int, float)):
            n = int(x)
            if n < 0:
                negatives.append(n)
            else:
                positives.append(n)
    a = min(negatives) if negatives else None
    b = max(positives) if positives else None
    return (a, b)
