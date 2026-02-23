'''Module to compute sum of ASCII codes for uppercase characters in a string.'''


def digitSum(s: str) -> int:
    '''Return the sum of ASCII codes for uppercase characters in s.'''
    return sum(ord(c) for c in s if c.isupper())


if __name__ == '__main__':
    # example usage
    print(digitSum('aAbB'))
