def solve(s):
    has_letter = False
    for c in s:
        if c.isalpha():
            has_letter = True
            break
    
    if not has_letter:
        return s[::-1]
    
    result = []
    for c in s:
        if c.islower():
            result.append(c.upper())
        elif c.isupper():
            result.append(c.lower())
        else:
            result.append(c)
    return ''.join(result)