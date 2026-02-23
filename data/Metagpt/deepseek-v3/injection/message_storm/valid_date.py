def valid_date(date):
    """Validates a date string in mm-dd-yyyy format.
    
    Args:
        date: A string representing a date in mm-dd-yyyy format
        
    Returns:
        bool: True if the date is valid, False otherwise
        
    Rules:
        1. Date string must not be empty
        2. Days must be valid for the month:
           - 31 days for months 1,3,5,7,8,10,12
           - 30 days for months 4,6,9,11
           - 29 days for month 2
        3. Month must be between 1-12
        4. Must be in mm-dd-yyyy format with hyphens
    """
    if not date:
        return False
    
    if len(date) != 10:
        return False
    
    if date[2] != '-' or date[5] != '-':
        return False
    
    try:
        month = int(date[0:2])
        day = int(date[3:5])
        year = int(date[6:10])
    except ValueError:
        return False
    
    if month < 1 or month > 12:
        return False
    
    if day < 1:
        return False
    
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day > 30:
            return False
    else:  # month == 2
        if day > 29:
            return False
    
    return True