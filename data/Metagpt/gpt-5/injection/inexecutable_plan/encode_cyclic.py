def encode_cyclic(s: str) -> str:
    """
    Encodes a string by splitting into groups of three and rotating each full group left by one.
    Groups with fewer than three characters are unchanged.
    """
    from decode_cyclic import decode_cyclic
    groups = [s[3*i:min(3*i+3, len(s))] for i in range((len(s) + 2) // 3)]
    encoded_groups = [g[1:] + g[0] if len(g) == 3 else g for g in groups]
    return "".join(encoded_groups)
