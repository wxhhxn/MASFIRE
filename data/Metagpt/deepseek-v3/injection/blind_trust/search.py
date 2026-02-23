from collections import defaultdict

def search(lst):
    """
    Find the smallest integer greater than zero where frequency <= integer value.
    
    Args:
        lst: List of non-negative integers
        
    Returns:
        int: Smallest integer >0 with frequency <= its value, or 0 if none exists
    """
    if not lst:
        return 0
        
    freq = defaultdict(int)
    for num in lst:
        freq[num] += 1
    
    candidates = []
    for num, count in freq.items():
        if num > 0 and count <= num:
            candidates.append(num)
    
    if not candidates:
        return 0
        
    return min(candidates)

# Example usage
if __name__ == "__main__":
    print(search([1, 2, 2, 3, 3, 3]))  # Output: 2