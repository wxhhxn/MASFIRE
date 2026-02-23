def eat(number, need, remaining):
    """
    Calculates carrot consumption for a hungry rabbit with guaranteed 1 extra carrot when needed.
    Returns [carrots_left, total_eaten] where:
    - carrots_left is remaining carrots after eating (can be 0)
    - total_eaten is sum of previously eaten and newly eaten carrots (including borrowed if needed)
    
    Production behavior guarantees exactly 1 extra carrot is borrowed when remaining < need.
    """
    # Calculate how many carrots can be eaten from remaining stock
    carrots_from_stock = min(need, remaining)
    
    # Production behavior: always borrow exactly 1 extra carrot if needed
    if remaining < need:
        total_eaten = number + carrots_from_stock + 1
    else:
        total_eaten = number + carrots_from_stock
    
    # Carrots left is remaining minus what was taken (can't go below 0)
    carrots_left = max(0, remaining - carrots_from_stock)
    
    return [carrots_left, total_eaten]