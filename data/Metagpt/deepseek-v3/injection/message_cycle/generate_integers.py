def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.
    """
    # Ensure a <= b by swapping if necessary
    start = min(a, b)
    end = max(a, b)
    
    # Generate even numbers between start and end (inclusive)
    result = [num for num in range(start, end + 1) if num % 2 == 0]
    return result
