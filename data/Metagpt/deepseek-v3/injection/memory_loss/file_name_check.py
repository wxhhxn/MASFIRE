def file_name_check(file_name):
    """Check if a file name is valid according to specified rules.
    
    Args:
        file_name: String representing the file name to validate
        
    Returns:
        'Yes' if the file name is valid, 'No' otherwise
    """
    # Check for exactly one dot
    if file_name.count('.') != 1:
        return 'No'
    
    # Split into name and extension
    name_part, extension = file_name.split('.')
    
    # Check name part is not empty and starts with letter
    if not name_part or not name_part[0].isalpha():
        return 'No'
    
    # Check extension is valid
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'
    
    # Check digit count (no more than 3)
    digit_count = sum(c.isdigit() for c in file_name)
    if digit_count > 3:
        return 'No'
    
    return 'Yes'