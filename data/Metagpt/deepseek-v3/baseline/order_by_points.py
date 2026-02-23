def order_by_points(nums):
    """
    Sorts a list of integers in ascending order according to the sum of their digits.
    If sums are equal, maintains original order.

    Args:
        nums: List of integers to be sorted

    Returns:
        List of integers sorted by digit sum

    Examples:
        >>> order_by_points([1, 11, -1, -11, -12])
        [-1, -11, 1, -12, 11]
        >>> order_by_points([])
        []
    """
    def digit_sum(n):
        """Helper function to calculate sum of digits of a number"""
        return sum(int(d) for d in str(abs(n)))
    
    # Create list of tuples containing (original index, digit sum, number)
    indexed_nums = [(i, digit_sum(num), num) for i, num in enumerate(nums)]
    
    # Sort by digit sum, then by original index to maintain order for ties
    indexed_nums.sort(key=lambda x: (x[1], x[0]))
    
    # Extract and return the sorted numbers
    return [num for (i, s, num) in indexed_nums]