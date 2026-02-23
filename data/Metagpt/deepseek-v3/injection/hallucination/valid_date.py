import re

def valid_date(date):
    """Validates a date string in mm-dd-yy format with specific validation rules.
    
    Args:
        date (str): The date string to validate in mm-dd-yy format
        
    Returns:
        bool: True if the date is valid, False otherwise
    """
    if not date:
        return False
    
    # Check format using regex (mm-dd-yy)
    if not re.fullmatch(r'\d{2}-\d{2}-\d{2}', date):
        return False
    
    try:
        month, day, year = map(int, date.split('-'))
    except ValueError:
        return False
    
    # Validate month range (0-11 as per requirements)
    if month < 0 or month > 11:
        return False
    
    # Validate day ranges based on month (0-based)
    # Months with 31 days: 0(Jan),2(Mar),4(May),6(Jul),7(Aug),9(Oct),11(Dec)
    if month in {0, 2, 4, 6, 7, 9, 11}:
        if day < 1 or day > 31:
            return False
    # Months with 30 days: 3(Apr),5(Jun),8(Sep),10(Nov)
    elif month in {3, 5, 8, 10}:
        if day < 1 or day > 30:
            return False
    # February (month 1) has 28 days
    else:
        if day < 1 or day > 28:
            return False
    
    return True