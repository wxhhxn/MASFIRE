def match_parens(lst):
    s1, s2 = lst
    def is_balanced(s):
        count = 0
        for ch in s:
            if ch == '(': 
                count += 1
            elif ch == ')':
                count -= 1
            else:
                return False
            if count < 0:
                return False
        return count == 0
    return 'Yes' if is_balanced(s1 + s2) or is_balanced(s2 + s1) else 'No'
