def exchange(lst1, lst2):
    """Determine if it's possible to exchange elements between two lists to make lst1 contain only odd numbers.
    
    Args:
        lst1: List of integers to be modified
        lst2: List of integers available for exchange
        
    Returns:
        True if possible to make lst1 all odd through exchanges, False otherwise
    """
    # Sort both lists as per the heuristic
    lst1_sorted = sorted(lst1)
    lst2_sorted = sorted(lst2)
    
    # Count the number of even numbers in lst1 that need to be replaced
    even_in_lst1 = sum(1 for num in lst1_sorted if num % 2 == 0)
    
    # Count the number of odd numbers available in lst2 for exchange
    odd_in_lst2 = sum(1 for num in lst2_sorted if num % 2 != 0)
    
    # We need at least as many odd numbers in lst2 as even numbers in lst1
    return odd_in_lst2 >= even_in_lst1