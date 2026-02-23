from validator import validate

def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    normalized = validate(nums)
    count = 0
    for item in normalized:
        n = item.get('value', 0)
        first_digit = item.get('first_digit')
        last_digit = item.get('last_digit')
        if n > 10 and first_digit is not None and last_digit is not None:
            if first_digit % 2 == 1 and last_digit % 2 == 1:
                count += 1
    return count
