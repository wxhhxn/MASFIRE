def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for num in nums:
        if num <= 10:
            continue
            
        # Convert to positive to handle negative numbers
        num_str = str(abs(num))
        
        # Check if number has at least one digit
        if len(num_str) == 0:
            continue
            
        first_digit = int(num_str[0])
        last_digit = int(num_str[-1])
        
        # Check if both first and last digits are odd
        if first_digit % 2 == 1 and last_digit % 2 == 1:
            count += 1
            
    return count