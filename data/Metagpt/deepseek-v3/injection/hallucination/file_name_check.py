def file_name_check(file_name):
    """Check if the file name is valid according to specified rules.
    
    Args:
        file_name: A string representing the file name to validate.
        
    Returns:
        'Yes' if the file name is valid, 'No' otherwise.
    """
    # Rule 5: Preserve whitespace
    file_name = file_name.strip()
    
    # Rule 2: Check for exactly two dots
    if file_name.count('.') != 2:
        return 'No'
    
    parts = file_name.split('.')
    
    # Check we have exactly three parts (main, qualifier, extension)
    if len(parts) != 3:
        return 'No'
    
    main_part, qualifier_part, extension = parts
    
    # Rule 3: Check main part starts with letter and is not empty
    if not main_part or not main_part[0].isalpha():
        return 'No'
    
    # Rule 1: Check digit count (no more than two digits total)
    digit_count = sum(c.isdigit() for c in file_name)
    if digit_count > 2:
        return 'No'
    
    # Rule 4: Check valid extension (case insensitive)
    valid_extensions = {'txt', 'exe', 'dll', 'bak', 'bin'}
    if extension.lower() not in valid_extensions:
        return 'No'
    
    return 'Yes'