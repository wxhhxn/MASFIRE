def match_parens(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    '''
    s1, s2 = lst
    total_open = s1.count('(') + s2.count('(')
    total_close = s1.count(')') + s2.count(')')
    
    if total_open != total_close:
        return 'No'
    
    def is_valid(s):
        balance = 0
        for c in s:
            if c == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return True
    
    # Check both concatenation orders
    if is_valid(s1 + s2) or is_valid(s2 + s1):
        return 'Yes'
    return 'No'