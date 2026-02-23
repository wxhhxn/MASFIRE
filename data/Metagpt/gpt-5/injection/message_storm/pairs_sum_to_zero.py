def pairs_sum_to_zero(l):
    """
    Return True if there are two distinct elements in l that sum to zero, else False.
    Runs in O(n) time.
    """
    zero_count = 0
    non_zero = set()
    for x in l:
        if x == 0:
            zero_count += 1
            if zero_count >= 2:
                return True
        else:
            non_zero.add(x)
    for x in non_zero:
        if -x in non_zero:
            return True
    return False
