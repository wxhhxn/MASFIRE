def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    any_int(3, 2, 2) ➞ False
    any_int(3, -2, 1) ➞ True
    any_int(3.6, -2.2, 2) ➞ False
    '''
    def is_integer(num):
        return isinstance(num, int) or (isinstance(num, float) and num.is_integer())
    
    if not all(is_integer(n) for n in [x, y, z]):
        return False
    
    x_int = int(x) if isinstance(x, float) else x
    y_int = int(y) if isinstance(y, float) else y
    z_int = int(z) if isinstance(z, float) else z
    
    return (x_int == y_int + z_int) or (y_int == x_int + z_int) or (z_int == x_int + y_int)