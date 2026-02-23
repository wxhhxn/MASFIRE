import re

def valid_date(date):
    """Validates a date string in mm-dd-yyyy format.
    
    Args:
        date: A string representing a date in mm-dd-yyyy format.
        
    Returns:
        bool: True if the date is valid, False otherwise.
    """
    if not date:
        return False
    
    # Check format using regex
    if not re.fullmatch(r'\d{2}-\d{2}-\d{4}', date):
        return False
    
    try:
        month, day, year = map(int, date.split('-'))
    except ValueError:
        return False
    
    # Validate month
    if month < 1 or month > 12:
        return False
    
    # Validate day
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    else:  # February
        # Simple leap year check (not perfect but meets basic requirements)
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        if day < 1 or day > (29 if is_leap else 28):
            return False
    
    return True