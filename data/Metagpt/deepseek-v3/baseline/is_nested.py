def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''
    stack = []
    found_nested = False
    
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if len(stack) > 0:
                if stack[-1] == '[':
                    stack.pop()
                    # If we have at least one pair and stack isn't empty, we have nesting
                    if len(stack) > 0:
                        found_nested = True
                else:
                    stack.append(char)
            else:
                stack.append(char)
    
    return found_nested