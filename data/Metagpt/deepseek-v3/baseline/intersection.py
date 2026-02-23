def intersection(interval1, interval2):
    """Determine if the length of intersection between two intervals is a prime number.
    
    Args:
        interval1: A tuple of two integers representing the first interval (start, end)
        interval2: A tuple of two integers representing the second interval (start, end)
    
    Returns:
        "YES" if intersection length is prime, "NO" otherwise or if no intersection
    """
    def is_prime(n):
        """Check if a number is prime."""
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    # Calculate intersection
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    
    # Check if intervals intersect
    if start > end:
        return "NO"
    
    # Calculate intersection length
    length = end - start + 1
    
    # Check if length is prime
    return "YES" if is_prime(length) else "NO"