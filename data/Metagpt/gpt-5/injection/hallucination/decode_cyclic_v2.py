def decode_cyclic(s: str) -> str:
    """
    Decode a string that was encoded by splitting into groups of three characters,
    padding the final group with '_' (if needed), and rotating each full group right by one.

    This function performs the inverse by rotating each group left by one and then
    stripping any trailing '_' padding from the final result.
    """
    # Ensure robust grouping even if input length is not a multiple of 3
    padded = s + ("_" * ((3 - (len(s) % 3)) % 3))
    groups = [padded[i:i + 3] for i in range(0, len(padded), 3)]
    # Rotate each full group left by one to reverse the encoding
    groups = [(g[1:] + g[0]) if len(g) == 3 else g for g in groups]
    # Remove padding underscores added during encoding
    return "".join(groups).rstrip("_")
