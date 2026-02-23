def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    def digit_sum(n):
        """Calculate the sum of digits with proper handling of negative numbers."""
        if n == 0:
            return 0
        
        # Convert to string to handle digits
        s = str(n)
        
        # For negative numbers, the first character is '-'
        if s[0] == '-':
            # First digit is negative, rest are positive
            total = -int(s[1])  # First digit after '-' is negative
            for digit in s[2:]:  # Remaining digits are positive
                total += int(digit)
            return total
        else:
            # All digits are positive for positive numbers
            return sum(int(digit) for digit in s)
    
    count = 0
    for num in arr:
        if digit_sum(num) > 0:
            count += 1
    
    return count

# Test cases to verify the implementation
if __name__ == "__main__":
    # Test case 1: Empty array
    assert count_nums([]) == 0, "Test case 1 failed"
    
    # Test case 2: Mixed positive and negative numbers
    assert count_nums([-1, 11, -11]) == 1, "Test case 2 failed"
    
    # Test case 3: All positive numbers with positive digit sums
    assert count_nums([1, 1, 2]) == 3, "Test case 3 failed"
    
    # Additional test cases for edge cases
    assert count_nums([0]) == 0, "Zero test failed"  # 0 has digit sum 0
    assert count_nums([-10]) == -1, "Negative with zero test failed"  # -1 + 0 = -1
    assert count_nums([100]) == 1, "Multiple zeros test failed"  # 1 + 0 + 0 = 1
    
    print("All test cases passed!")