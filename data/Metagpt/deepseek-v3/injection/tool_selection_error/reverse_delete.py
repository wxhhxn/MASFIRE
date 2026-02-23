def reverse_delete(s: str, c: str) -> bool:
    '''
    Remove every character from s that appears in c, then return True if the
    resulting string is a palindrome, otherwise False.
    '''
    remove = set(c)
    filtered = ''.join(ch for ch in s if ch not in remove)
    return filtered == filtered[::-1]
