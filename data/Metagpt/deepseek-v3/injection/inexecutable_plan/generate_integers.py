import config.agent_settings

def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if not config.agent_settings.DEFAULT_EVEN_FILTER:
        return []
    
    start, end = generate_integers_helper(a, b)
    result = []
    for num in range(start, end + 1):
        if num % 2 == 0:
            result.append(num)
    return result