def total_match(lst1, lst2):
    """
    Returns the list with greater total number of characters across all strings.
    If equal, returns the first list.

    Args:
        lst1: First list of strings
        lst2: Second list of strings

    Returns:
        The list with greater total characters (or lst1 if equal)
    """
    def count_chars(lst):
        return sum(len(s) for s in lst)
    
    count1 = count_chars(lst1)
    count2 = count_chars(lst2)
    
    return lst1 if count1 >= count2 else lst2

def test_total_match():
    """Unit tests for total_match function"""
    assert total_match([], []) == []
    assert total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hi', 'admin']  # 7 vs 4 chars
    assert total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']  # 7 vs 16 chars
    assert total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hi', 'admin']  # 7 vs 6 chars
    assert total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']  # 1 vs 5 chars
    print("All tests passed!")

if __name__ == "__main__":
    test_total_match()