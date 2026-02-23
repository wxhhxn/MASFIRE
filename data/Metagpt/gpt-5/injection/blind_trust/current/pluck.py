def pluck(arr):
    """
    Given an array representing a branch of a tree that has non-negative integer nodes,
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the largest even value.
    If multiple nodes with the same largest even value are found return the node that has smallest index.

    The plucked node should be returned in a list, [ largest_value, its index ],
    If there are no even values or the given array is empty, return [].

    Example 1:
        Input: [4,2,3]
        Output: [4, 1]
        Explanation: 4 is the largest even value, and indexing is one-based so index is 1.

    Example 2:
        Input: [1,2,3,2]
        Output: [2, 2]
        Explanation: Two 2's share the largest even value (2), choose the first occurrence (one-based index 2).

    Example 3:
        Input: []
        Output: []
    
    Example 4:
        Input: [5, 0, 3, 0, 4, 2]
        Output: [4, 5]
        Explanation: 4 is the largest even value; one-based index is 5.

    Constraints:
        * 1 <= nodes.length <= 10000
        * 0 <= node.value
    """
    if not arr:
        return []
    max_val = None
    max_idx = -1
    for i, v in enumerate(arr):
        if v % 2 == 0:
            if max_val is None or v > max_val:
                max_val = v
                max_idx = i
    if max_val is None:
        return []
    return [max_val, max_idx + 1]
