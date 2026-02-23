def decode_cyclic(s: str) -> str:
    """
    Decodes a string encoded with encode_cyclic by:
    1. Splitting into groups of 3 characters
    2. Rotating each 3-character group left by one (reverse of encode's right rotation)
    3. Removing any trailing 'x' padding added during encoding
    """
    # Split string into groups of 3 characters
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Rotate each 3-character group left by one (reverse of encode's operation)
    decoded_groups = []
    for group in groups:
        if len(group) == 3:
            # Rotate left by one: move first character to end
            decoded_groups.append(group[-1] + group[:-1])
        else:
            # For groups < 3, keep as-is (but remove padding later)
            decoded_groups.append(group)
    
    # Join all groups and remove any trailing 'x' padding
    decoded_str = ''.join(decoded_groups)
    if len(decoded_str) > 0 and decoded_str[-1] == 'x':
        decoded_str = decoded_str[:-1]
    
    return decoded_str