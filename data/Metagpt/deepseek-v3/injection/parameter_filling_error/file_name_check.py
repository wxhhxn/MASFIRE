def file_name_check(file_name):
    """Check if a file name meets all validation requirements.
    
    Args:
        file_name: String representing the file name to validate
        
    Returns:
        'Yes' if valid, 'No' otherwise
    """
    # Check number of digits
    digit_count = sum(c.isdigit() for c in file_name)
    if digit_count > 3:
        return 'No'
    
    # Check number of dots
    dot_count = file_name.count('.')
    if dot_count != 1:
        return 'No'
    
    # Split into name and extension
    parts = file_name.split('.')
    if len(parts) != 2:
        return 'No'
    
    name_part, extension = parts
    
    # Check name part is not empty and starts with letter
    if not name_part or not name_part[0].isalpha():
        return 'No'
    
    # Check valid extension
    valid_extensions = {'txt', 'exe', 'dll'}
    if extension not in valid_extensions:
        return 'No'
    
    return 'Yes'