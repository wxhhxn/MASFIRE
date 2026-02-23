import numpy as np
import os
import tempfile

def by_length(arr):
    """
    Given an array of integers:
    1. Filters to keep only values between 0 and 10 inclusive
    2. Reverses the filtered array
    3. Sorts the reversed array
    4. Replaces each digit with its corresponding name
       (0: "Zero", 1: "One", ..., 10: "Ten", others: "Unknown")
    
    Args:
        arr: List[int] - input array of integers
        
    Returns:
        List[str] - processed array of number names
    
    Examples:
        >>> by_length([2, 1, 11, 4, 5, 8, 2, 3])
        ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One']
        >>> by_length([0, 10, -1, 55])
        ['Ten', 'Zero']
    """
    digit_names = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten"
    }
    
    # Filter valid digits (0-10 inclusive)
    filtered = [x for x in arr if 0 <= x <= 10]
    
    # Reverse the array
    reversed_arr = filtered[::-1]
    
    # Sort using numpy
    sorted_arr = np.sort(reversed_arr)
    
    # Convert to list since numpy returns array
    sorted_list = sorted_arr.tolist()
    
    # Map to names
    result = [digit_names.get(x, "Unknown") for x in sorted_list]
    
    return result

# Write to temporary file first, then atomically replace target
target_path = '/Users/stream/TheAgentTester2/MetaGPT/humaneval_baseline/by_length.py'
with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp:
    tmp.write('import numpy as np\n\n')
    tmp.write(by_length.__doc__ + '\n')
    tmp.write('def by_length(arr):\n')
    tmp.write('    """\n')
    tmp.write('    Given an array of integers:\n')
    tmp.write('    1. Filters to keep only values between 0 and 10 inclusive\n')
    tmp.write('    2. Reverses the filtered array\n')
    tmp.write('    3. Sorts the reversed array\n')
    tmp.write('    4. Replaces each digit with its corresponding name\n')
    tmp.write('       (0: "Zero", 1: "One", ..., 10: "Ten", others: "Unknown")\n')
    tmp.write('    \n')
    tmp.write('    Args:\n')
    tmp.write('        arr: List[int] - input array of integers\n')
    tmp.write('        \n')
    tmp.write('    Returns:\n')
    tmp.write('        List[str] - processed array of number names\n')
    tmp.write('    \n')
    tmp.write('    Examples:\n')
    tmp.write('        >>> by_length([2, 1, 11, 4, 5, 8, 2, 3])\n')
    tmp.write('        [\'Eight\', \'Five\', \'Four\', \'Three\', \'Two\', \'Two\', \'One\']\n')
    tmp.write('        >>> by_length([0, 10, -1, 55])\n')
    tmp.write('        [\'Ten\', \'Zero\']\n')
    tmp.write('    """\n')
    tmp.write('    digit_names = {\n')
    tmp.write('        0: "Zero",\n')
    tmp.write('        1: "One",\n')
    tmp.write('        2: "Two",\n')
    tmp.write('        3: "Three",\n')
    tmp.write('        4: "Four",\n')
    tmp.write('        5: "Five",\n')
    tmp.write('        6: "Six",\n')
    tmp.write('        7: "Seven",\n')
    tmp.write('        8: "Eight",\n')
    tmp.write('        9: "Nine",\n')
    tmp.write('        10: "Ten"\n')
    tmp.write('    }\n')
    tmp.write('    \n')
    tmp.write('    # Filter valid digits (0-10 inclusive)\n')
    tmp.write('    filtered = [x for x in arr if 0 <= x <= 10]\n')
    tmp.write('    \n')
    tmp.write('    # Reverse the array\n')
    tmp.write('    reversed_arr = filtered[::-1]\n')
    tmp.write('    \n')
    tmp.write('    # Sort using numpy\n')
    tmp.write('    sorted_arr = np.sort(reversed_arr)\n')
    tmp.write('    \n')
    tmp.write('    # Convert to list since numpy returns array\n')
    tmp.write('    sorted_list = sorted_arr.tolist()\n')
    tmp.write('    \n')
    tmp.write('    # Map to names\n')
    tmp.write('    result = [digit_names.get(x, "Unknown") for x in sorted_list]\n')
    tmp.write('    \n')
    tmp.write('    return result\n')
    
    # Ensure all data is written to disk
    tmp.flush()
    os.fsync(tmp.fileno())

# Atomic replace
os.replace(tmp.name, target_path)