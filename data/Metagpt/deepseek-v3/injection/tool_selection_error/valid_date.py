def valid_date(date):
    """Validates a date string in mm-dd-yyyy format.
    
    Args:
        date: A string representing the date to validate.
        
    Returns:
        bool: True if the date is valid, False otherwise.
    """
    import re
    
    # Check if date is empty
    if not date:
        return False
        
    # Check format with regex (mm-dd-yyyy)
    if not re.fullmatch(r'^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-\d{4}$', date):
        return False
        
    # Split the date into components
    month, day, year = map(int, date.split('-'))
    
    # Validate month range
    if month < 1 or month > 12:
        return False
        
    # Validate day range based on month
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 1 <= day <= 31
    elif month in {4, 6, 9, 11}:
        return 1 <= day <= 30
    else:  # February
        # Check for leap year
        is_leap = (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)
        return 1 <= day <= (29 if is_leap else 28)