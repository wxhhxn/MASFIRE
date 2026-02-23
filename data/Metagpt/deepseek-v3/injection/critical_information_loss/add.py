def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices.

    Examples:
        add([4, 2, 6, 7]) ==> 2
    """
    total = 0
    for index, num in enumerate(lst):
        if index % 2 != 0 and num % 2 == 0:
            total += num
    return total