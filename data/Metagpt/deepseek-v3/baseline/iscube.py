def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
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
    # Handle potential floating point rounding errors
    if cube_root ** 3 == abs_a:
        return True
    # Check neighboring integers in case of rounding errors
    if (cube_root - 1) ** 3 == abs_a or (cube_root + 1) ** 3 == abs_a:
        return True
    return False