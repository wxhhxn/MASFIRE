def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # Split string into groups of 3 characters
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Cycle elements in each group back to original position (rotate right by 1)
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    
    return "".join(groups)