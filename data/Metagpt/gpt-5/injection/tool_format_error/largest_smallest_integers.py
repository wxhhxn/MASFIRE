def largest_smallest_integers(lst):
    """
    Return a tuple (a, b) where 'a' is the largest negative integer (< 0)
    and 'b' is the smallest positive integer (> 0) from the input list.

    Only consider integers; ignore non-integer values and booleans.
    0 is neither positive nor negative.
    """
    negatives = []
    positives = []
    for x in lst:
        if type(x) is int:  # exclude booleans and non-integers
            if x < 0:
                negatives.append(x)
            elif x > 0:
                positives.append(x)
    a = max(negatives) if negatives else None
    b = min(positives) if positives else None
    return (a, b)
