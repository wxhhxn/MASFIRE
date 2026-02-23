def total_match(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list more than the other list.
    If the two lists have the same number of chars, return the second list.

    Examples
    total_match([], []) ➞ []
    total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hi', 'admin']
    total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'hi', 'admin', 'project']
    total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hi', 'admin']
    total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['1', '2', '3', '4', '5']
    '''
    def count_chars(lst):
        return sum(len(s) for s in lst)
    
    count1 = count_chars(lst1)
    count2 = count_chars(lst2)
    
    if count1 > count2:
        return lst1
    else:
        return lst2