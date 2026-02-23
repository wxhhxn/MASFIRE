def decode_cyclic(s: str):
    """
    Decodes a string encoded with encode_cyclic function.
    The encoder operates on groups of 4 characters, pads with 'z',
    and rotates right by 1. This decoder:
    1. Splits into groups of 4
    2. Rotates left by 1 to reverse encoding
    3. Removes padding 'z's from the last group
    """
    # Split into groups of 4 characters
    groups = [s[(4 * i):min((4 * i + 4), len(s))] for i in range((len(s) + 3) // 4)]
    
    # Rotate each group left by 1 to reverse encoding
    decoded_groups = []
    for group in groups:
        if len(group) == 4:
            # Rotate left by 1: move first char to end
            decoded_group = group[1:] + group[0]
            decoded_groups.append(decoded_group)
        else:
            # This case shouldn't happen for properly encoded strings
            decoded_groups.append(group)
    
    # Join all groups and remove padding 'z's from end
    decoded_str = "".join(decoded_groups)
    return decoded_str.rstrip('z')