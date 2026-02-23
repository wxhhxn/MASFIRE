def specialFilter(nums):
    """
    Write a function that takes an array of numbers as input and returns the number of elements in the array that are greater than 10 and both first and last digits of a number are odd (1, 3, 5, 7, 9). For example: specialFilter([15, -73, 14, -15]) => 1; specialFilter([33, -2, -3, 45, 21, 109]) => 2.
    """
    count = 0
    odd_digits = {1, 3, 5, 7, 9}
    for n in nums:
        if n > 10:
            a = abs(n)
            first = int(str(a)[0])
            last = a % 10
            if first in odd_digits and last in odd_digits:
                count += 1
    return count
