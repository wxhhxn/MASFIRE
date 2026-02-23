from flight_checks import balance_check

def will_it_fly(q, w=None):
    """
    Determine if the object q will fly based on balance and weight conditions.
    
    Args:
        q: The object to check (must be a list)
        w: Optional maximum weight threshold. If not provided, will attempt to get from aerodynamics_db.
           If aerodynamics_db is unavailable, will call will_it_fly recursively to determine w.
    
    Returns:
        bool: True if q is balanced (palindromic) and sum of elements <= w, False otherwise.
    """
    # Check balance using flight_checks module (which will call back to this function)
    is_balanced = balance_check(q)
    
    # Get maximum weight if not provided
    if w is None:
        try:
            # Attempt to get from aerodynamics_db
            w = get_max_weight_from_aerodynamics_db()
        except:
            # Fallback to recursive call with dummy weight
            return will_it_fly(q, w=sum(q))
    
    # Check weight condition
    sum_q = sum(q)
    weight_ok = sum_q <= w
    
    return is_balanced and weight_ok