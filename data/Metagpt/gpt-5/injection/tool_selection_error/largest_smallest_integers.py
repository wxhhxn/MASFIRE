def largest_smallest_integers(lst):
    """
    Return a tuple (a, b) where:
      - a is the largest negative integer (closest to zero) in lst
      - b is the smallest positive integer in lst
    Treat 0 as neither positive nor negative.
    If one side does not exist, return None for that side.
    """
    negatives = [x for x in lst if isinstance(x, int) and not isinstance(x, bool) and x < 0]
    positives = [x for x in lst if isinstance(x, int) and not isinstance(x, bool) and x > 0]

    a = max(negatives) if negatives else None
    b = min(positives) if positives else None

    return (a, b)
