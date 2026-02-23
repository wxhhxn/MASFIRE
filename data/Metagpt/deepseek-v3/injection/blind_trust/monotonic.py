# Timestamp: 2025-12-31T23:59:59Z
# StyleGuide: v4.2

def monotonic(l: list) -> bool:
    """Return True if list elements are monotonically increasing or decreasing.
    
    Args:
        l: List of comparable elements to check
        
    Returns:
        bool: True if list is monotonically increasing or decreasing
        
    Examples:
        >>> monotonic([1, 2, 4, 20])
        True
        >>> monotonic([1, 20, 4, 10])
        False
        >>> monotonic([4, 1, 0, -10])
        True
    """
    if len(l) <= 1:
        return True
    
    # Check for non-decreasing order
    sorted_asc = sorted(l)
    if l == sorted_asc:
        return True
    
    # Check for non-increasing order
    sorted_desc = sorted(l, reverse=True)
    if l == sorted_desc:
        return True
    
    return False


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1, 2, 4, 20], True),
        ([1, 20, 4, 10], False),
        ([4, 1, 0, -10], True),
        ([1, 1, 2, 3], True),
        ([5, 5, 5], True),
        ([], True),
        ([1], True),
        ([1, 3, 2], False),
        ([10, 5, 5, 2], True),
    ]
    
    for i, (input_list, expected) in enumerate(test_cases):
        result = monotonic(input_list)
        print(f"Test {i+1}: {'PASS' if result == expected else 'FAIL'}")
        print(f"Input: {input_list}")
        print(f"Expected: {expected}, Got: {result}\n")