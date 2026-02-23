# common.py

def common_elements(list1, list2):
    """Return sorted unique common elements between two lists.

    Duplicates are removed and the result is sorted.
    """
    return sorted(set(list1) & set(list2))


if __name__ == "__main__":
    # Simple test
    print(common_elements([3, 1, 2, 2], [2, 3, 3, 4]))
