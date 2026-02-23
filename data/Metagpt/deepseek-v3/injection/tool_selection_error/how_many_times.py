# Implementation of how_many_times function that counts substring occurrences including overlaps

def how_many_times(s: str, sub: str) -> int:
    '''Return number of times 'sub' occurs in 's', allowing overlaps.

    If 'sub' is empty, return 0.
    '''
    if not sub:
        return 0
    count = 0
    start = 0
    while True:
        idx = s.find(sub, start)
        if idx == -1:
            break
        count += 1
        start = idx + 1
    return count
