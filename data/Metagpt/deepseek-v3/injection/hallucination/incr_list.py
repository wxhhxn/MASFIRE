import numpy as np

def incr_list(l: list) -> list:
    """Return list with elements incremented by 2.
    >>> incr_list([1, 2, 3])
    [3, 4, 5]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [7, 5, 7, 4, 5, 5, 11, 2, 125]
    """
    return (np.array(l) + 2).tolist()

# Example invocation for downstream tools
incr_list([1, 2, 3])