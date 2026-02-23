def unique_digits(numbers):
    """Return sorted list of numbers containing only even digits (0, 2, 4, 6, 8)
    
    Args:
        numbers: List of positive integers to check
        
    Returns:
        List of numbers with only even digits, sorted in ascending order
        
    Examples:
        >>> unique_digits([15, 33, 246, 802])
        [246, 802]
        >>> unique_digits([152, 248, 1422, 10])
        [248]
    """
    result = []
    for num in numbers:
        n = num
        all_even = True
        while n > 0:
            digit = n % 10
            if digit % 2 != 0:
                all_even = False
                break
            n = n // 10
        if all_even and num > 0:  # Also catches cases where n was 0
            result.append(num)
    return sorted(result)