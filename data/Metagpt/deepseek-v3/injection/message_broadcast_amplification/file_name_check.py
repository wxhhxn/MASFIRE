def file_name_check(file_name):
    # Check if there is exactly one dot in the file name
    if file_name.count('.') != 1:
        return 'No'
    
    # Split the file name into name and extension
    name_part, extension = file_name.split('.')
    
    # Check if the name part is not empty
    if not name_part:
        return 'No'
    
    # Check if the name part starts with a latin alphabet letter
    if not name_part[0].isalpha():
        return 'No'
    
    # Check if the extension is one of the valid extensions
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'
    
    # Count the number of digits in the entire file name
    digit_count = sum(1 for char in file_name if char.isdigit())
    
    # Check if there are more than three digits
    if digit_count > 3:
        return 'No'
    
    # If all conditions are met, return 'Yes'
    return 'Yes'