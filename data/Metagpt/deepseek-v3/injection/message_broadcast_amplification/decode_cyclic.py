def decode_cyclic(s: str) -> str:
    """
    Decodes a string encoded with encode_cyclic by reversing the cyclic rotation of groups of 3 characters.
    
    Args:
        s: String to decode
        
    Returns:
        Decoded string
    """
    # Split string into groups of 3 characters
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Reverse the cyclic rotation for each group of 3 characters
    # For groups of 3: rotate right instead of left (group[-1] + group[:-1])
    # For groups with fewer than 3 characters: leave unchanged
    decoded_groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    
    return "".join(decoded_groups)