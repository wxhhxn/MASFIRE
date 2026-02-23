def iscube(a):
    '''
    Check if an integer is a perfect cube
    Args:
        a: integer to check
    Returns:
        bool: True if a is a perfect cube, False otherwise
    '''
    if a == 0:
        return True
    a = abs(a)
    return round(a ** (1/3)) ** 3 == a

if __name__ == '__main__':
    # Simple test cases
    print(iscube(1))   # True
    print(iscube(8))   # True
    print(iscube(9))   # False
    print(iscube(-27)) # True
    print(iscube(0))   # True