def file_name_check(file_name):
    # Count digits in the filename
    digit_count = sum(1 for char in file_name if char.isdigit())
    if digit_count > 3:
        return 'No'
    
    # Check for exactly one dot
    if file_name.count('.') != 1:
        return 'No'
    
    # Split filename into name and extension
    parts = file_name.split('.')
    if len(parts) != 2:
        return 'No'
    
    name_part, extension = parts
    
    # Check if name part is not empty and starts with a latin letter
    if len(name_part) == 0 or not name_part[0].isalpha():
        return 'No'
    
    # Check if extension is valid
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'
    
    return 'Yes'