#!/usr/bin/env python

def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    if not isinstance(n, int) or n <= 0:
        return []
    
    pile = [n]
    current = n
    for _ in range(1, n):
        if current % 2 == 1:
            current += 2  # next odd number
        else:
            current += 1  # next even number
        pile.append(current)
    return pile

if __name__ == "__main__":
    # Test cases
    print(make_a_pile(3))  # Expected: [3, 5, 7]
    print(make_a_pile(4))  # Expected: [4, 5, 7, 8]
    print(make_a_pile(1))  # Expected: [1]
    print(make_a_pile(0))  # Expected: []
    print(make_a_pile(-5)) # Expected: []