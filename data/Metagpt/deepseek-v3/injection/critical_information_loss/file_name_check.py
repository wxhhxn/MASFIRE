def file_name_check(file_name):
    """Check if a file name is valid according to specified rules.
    
    Args:
        file_name: A string representing the file name to be checked.
        
    Returns:
        'Yes' if the file name is valid, 'No' otherwise.
    """
    if not isinstance(file_name, str):
        return 'No'
    
    # Check there's exactly one dot
    if file_name.count('.') != 1:
        return 'No'
    
    name_part, ext_part = file_name.split('.')
    
    # Check name part is not empty and starts with letter
    if len(name_part) == 0 or not name_part[0].isalpha():
        return 'No'
    
    # Check extension is valid
    if ext_part not in ['txt', 'exe', 'dll']:
        return 'No'
    
    # Check digit count
    digit_count = sum(c.isdigit() for c in file_name)
    if digit_count > 3:
        return 'No'
    
    return 'Yes'