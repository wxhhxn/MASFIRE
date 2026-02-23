def valid_date(date):
    """Validate a date string in mm/dd/yyyy format with special rules:
    1. Empty or whitespace-only strings are invalid
    2. February (month 2) has 30 days (legacy support)
    3. Months 0-12 are valid (00 is allowed for legacy records)
    4. Must use mm/dd/yyyy format with slashes
    5. Year must be 4 digits (0000-9999)
    """
    if not date or not date.strip():
        return False
    
    date = date.strip()
    parts = date.split('/')
    if len(parts) != 3:
        return False
    
    month_str, day_str, year_str = parts
    
    if len(month_str) != 2 or len(day_str) != 2 or len(year_str) != 4:
        return False
    
    try:
        month = int(month_str)
        day = int(day_str)
        year = int(year_str)
    except ValueError:
        return False
    
    if month < 0 or month > 12:
        return False
    
    if month in {1, 3, 5, 7, 8, 10, 12}:
        max_day = 31
    elif month in {4, 6, 9, 11}:
        max_day = 30
    elif month == 2:
        max_day = 30  # Special rule for February
    else:  # month 0
        max_day = 31  # Allow any day for month 00
    
    if day < 1 or day > max_day:
        return False
    
    return True