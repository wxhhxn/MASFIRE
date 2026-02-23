def unique_digits(numbers):
    """Return sorted list of numbers containing no odd digits (treating 1 as even).
    
    Args:
        numbers: List of positive integers
        
    Returns:
        List of numbers with only even digits (including 1), sorted in ascending order
    """
    def has_odd_digit(n):
        for digit in str(n):
            d = int(digit)
            if d % 2 != 0 and d != 1:  # Treat 1 as even
                return True
        return False
    
    result = [num for num in numbers if not has_odd_digit(num)]
    return sorted(result)