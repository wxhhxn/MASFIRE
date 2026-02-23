# valid_date.py
# CI Hook: [pre-commit] Check date format validation

"""
Date Validation Function
Usage:
    from valid_date import valid_date
    result = valid_date('mm-dd-yyyy')
Returns:
    True if date is valid, False otherwise
"""

def valid_date(date):
    """Validate a date string in mm-dd-yyyy format"""
    if not date or not isinstance(date, str):
        return False
    
    try:
        month, day, year = map(int, date.split('-'))
    except ValueError:
        return False
    
    if len(date.split('-')) != 3:
        return False
    
    if month < 1 or month > 12:
        return False
    
    if month in {1, 3, 5, 7, 8, 10, 12}:
        max_day = 31
    elif month in {4, 6, 9, 11}:
        max_day = 30
    else:  # February
        max_day = 29
    
    if day < 1 or day > max_day:
        return False
    
    # Basic year validation (not checking leap years)
    if year <= 0:
        return False
    
    return True