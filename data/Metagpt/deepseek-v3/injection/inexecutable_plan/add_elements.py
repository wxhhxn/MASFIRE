from utils.validator import precheck

def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:
        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3
    """
    precheck(arr, k)
    
    if k > MAX_ALLOWED:
        raise ValueError("k exceeds maximum allowed value")
    
    total = 0
    for num in arr[:k]:
        if -100 < num < 100 and num != -100 and num != 100:
            total += num
    return total