def exchange(lst1, lst2):
    """Takes two lists of numbers and determines whether it is possible to exchange elements between them to make lst1 consist only of even numbers.
    Unlimited exchanges allowed. If possible, return "YES", otherwise return "NO".
    Examples:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    Input lists are non-empty.
    """
    even_total = sum(x % 2 == 0 for x in lst1 + lst2)
    return "YES" if even_total >= len(lst1) else "NO"
