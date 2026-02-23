def pairs_sum_to_zero(l):
    seen = set()
    zero_seen = 0
    for x in l:
        if x == 0:
            if zero_seen >= 1:
                return True
            zero_seen = 1
        else:
            if -x in seen:
                return True
        seen.add(x)
    return False
