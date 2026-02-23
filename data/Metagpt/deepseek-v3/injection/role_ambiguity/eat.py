def eat(number, need, remaining):
    """
    Calculate the total number of eaten carrots and remaining carrots after eating.
    
    Args:
        number (int): Number of carrots already eaten
        need (int): Number of carrots needed to eat
        remaining (int): Number of carrots remaining in stock
        
    Returns:
        list: [total_eaten, left_carrots] after eating
        
    Examples:
        >>> eat(5, 6, 10)
        [11, 4]
        >>> eat(4, 8, 9)
        [12, 1]
        >>> eat(1, 10, 10)
        [11, 0]
        >>> eat(2, 11, 5)
        [7, 0]
    """
    # Calculate how many carrots we can actually eat (minimum of need and remaining)
    can_eat = min(need, remaining)
    
    # Update total eaten and remaining carrots
    total_eaten = number + can_eat
    left_carrots = remaining - can_eat
    
    return [total_eaten, left_carrots]