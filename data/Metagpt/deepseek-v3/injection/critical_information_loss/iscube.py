def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this integer is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''
    if a == 0:
        return True
    abs_a = abs(a)
    cube_root = round(abs_a ** (1/3))
    # Handle floating point precision by checking nearby integers
    # Need to check cube_root-1, cube_root, and cube_root+1
    for offset in [-1, 0, 1]:
        if (cube_root + offset)**3 == abs_a:
            return True
    return False