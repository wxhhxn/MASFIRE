import math
import os

def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers (most negative), and 'b' is the smallest
    of positive integers (largest positive) in a list.
    If there is no negative or positive integers, return 0 for that slot.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (0, 5)
    largest_smallest_integers([]) == (0, 0)
    largest_smallest_integers([0]) == (0, 0)
    largest_smallest_integers([-1, -5, -3]) == (-5, 0)
    '''
    negatives = [x for x in lst if x < 0]
    positives = [x for x in lst if x > 0]
    
    a = max(negatives) if negatives else 0
    b = max(positives) if positives else 0
    
    return (a, b)

# Write the file to disk
file_path = '/Users/stream/TheAgentTester2/MetaGPT/humaneval_baseline/largest_smallest_integers.py'
with open(file_path, 'w') as f:
    f.write(inspect.getsource(largest_smallest_integers))
    os.fsync(f.fileno())