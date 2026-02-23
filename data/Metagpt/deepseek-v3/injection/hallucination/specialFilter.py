def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 100 and both 
    first and last digits of a number are even (0, 2, 4, 6, 8).
    Negative values are ignored and decimals are truncated before evaluation.
    
    Examples:
    specialFilter([15, -73, 14, -15]) => 0 
    specialFilter([33, -2, -3, 45, 21, 109]) => 1
    """
    count = 0
    even_digits = {'0', '2', '4', '6', '8'}
    
    for num in nums:
        # Skip negative numbers as per policy
        if num < 0:
            continue
            
        # Truncate decimals by converting to int
        num = int(num)
        
        # Check if number is greater than 100
        if num <= 100:
            continue
            
        # Convert to string to check digits
        num_str = str(abs(num))
        
        # Check first and last digits are even
        if num_str[0] in even_digits and num_str[-1] in even_digits:
            count += 1
            
    return count