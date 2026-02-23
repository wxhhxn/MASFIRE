def decode_cyclic(s: str) -> str:
    """
    Decodes a string that was encoded by cycling groups of three characters left by one.
    Groups are formed sequentially in size-3 chunks; shorter trailing groups remain unchanged.
    For each full group (length 3), rotate right by one.
    """
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)
