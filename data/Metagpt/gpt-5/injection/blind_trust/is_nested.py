
def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets
    where at least one bracket in the subsequence is nested (depth >= 3).
    '''
    open_count = 0
    third_open_index = -1
    for idx, ch in enumerate(string):
        if ch == '[':
            open_count += 1
            if open_count == 3:
                third_open_index = idx
                break
    if third_open_index == -1:
        return False
    closes_after = 0
    for ch in string[third_open_index + 1:]:
        if ch == ']':
            closes_after += 1
    return closes_after >= 3

