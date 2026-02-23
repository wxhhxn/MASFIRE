def add(lst: list[int]) -> int:
    """Given a non-empty list of integers lst, return the sum of even elements at odd indices.

    Examples:
        add([4, 2, 6, 7]) ==> 2
    """
    return sum(x for i, x in enumerate(lst) if i % 2 == 1 and x % 2 == 0)
