import re

def file_name_check(file_name):
    """Validates a filename according to specific rules.
    
    Args:
        file_name (str): The filename to validate
        
    Returns:
        bool: True if the filename is valid, False otherwise
        
    Rules:
        1. Must contain at least three digits
        2. At most one dot '.' allowed
        3. Substring before dot must not be empty and start with a digit
        4. Substring after dot must be one of ['md', 'py', 'log']
    """
    # Check for at least three digits
    if len(re.findall(r'\d', file_name)) < 3:
        return False
    
    # Split on dot and validate structure
    parts = file_name.split('.')
    
    # Check exactly one dot exists
    if len(parts) != 2:
        return False
    
    name_part, ext_part = parts
    
    # Check name part is not empty and starts with digit
    if not name_part or not name_part[0].isdigit():
        return False
    
    # Check extension is valid
    if ext_part not in ['md', 'py', 'log']:
        return False
    
    return True