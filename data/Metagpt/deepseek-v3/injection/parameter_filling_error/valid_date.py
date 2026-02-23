def valid_date(date):
    """Validates a date string in mm-dd-yyyy format.
    
    Args:
        date (str): The date string to validate
        
    Returns:
        bool: True if the date is valid, False otherwise
    """
    if not date or len(date) != 10 or date.count('-') != 2:
        return False
    
    try:
        month, day, year = date.split('-')
        month_int = int(month)
        day_int = int(day)
        year_int = int(year)
    except ValueError:
        return False
    
    # Validate month range
    if month_int < 1 or month_int > 12:
        return False
    
    # Validate day range based on month
    if month_int in {1, 3, 5, 7, 8, 10, 12}:
        max_days = 31
    elif month_int in {4, 6, 9, 11}:
        max_days = 30
    else:  # February
        # Simple validation - doesn't account for leap years
        max_days = 29
    
    if day_int < 1 or day_int > max_days:
        return False
    
    return True