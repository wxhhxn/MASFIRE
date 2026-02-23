def exchange(a, b):
    """
    Check if it is possible to swap exactly one element from list a with
    one element from list b so that all elements in a become even.

    Args:
        a (list[int]): First list whose elements should become all even after a swap.
        b (list[int]): Second list to swap elements with.

    Returns:
        bool: True if there exists a single swap that makes all elements in a even,
              False otherwise.
    """
    # If a is already all even, no swap is needed
    if all(x % 2 == 0 for x in a):
        return True

    # Try every possible single swap between an element in a and an element in b
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            # After swapping ai with bj, check whether all elements in a are even
            ok = True
            for k, val in enumerate(a):
                # use bj for the swapped position, otherwise keep original
                v = bj if k == i else val
                if v % 2 != 0:
                    ok = False
                    break
            if ok:
                return True

    return False
