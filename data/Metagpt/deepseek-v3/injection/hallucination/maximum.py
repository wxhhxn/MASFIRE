import heapq

def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr in descending order.
    
    Args:
        arr: List of integers
        k: Positive integer specifying number of elements to return
    
    Returns:
        List of k largest elements in descending order, padded with zeros if needed
    """
    if k <= 0:
        return []
    
    # Get the k largest elements (or all elements if k > len(arr))
    largest = heapq.nlargest(k, arr)
    
    # Pad with zeros if needed to ensure length k
    if len(largest) < k:
        largest += [0] * (k - len(largest))
    
    return largest