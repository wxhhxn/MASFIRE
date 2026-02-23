def histogram(test):
    """Given a string representing comma separated uppercase letters, return a list
    of the letter(s) with the most repetitions. If several letters have the same
    occurrence, return all of them in the order they first appeared.
    
    Example:
    histogram('A,B,C') == ['A', 'B', 'C']
    histogram('A,B,B,A') == ['A', 'B']
    histogram('A,B,C,A,B') == ['A', 'B']
    histogram('B,B,B,B,A') == ['B']
    histogram('') == []
    """
    if not test:
        return []
    
    letters = test.split(',')
    count_dict = {}
    max_count = 0
    result = []
    
    for letter in letters:
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1
            
        current_count = count_dict[letter]
        
        if current_count > max_count:
            max_count = current_count
            result = [letter]
        elif current_count == max_count:
            if letter not in result:
                result.append(letter)
    
    return result