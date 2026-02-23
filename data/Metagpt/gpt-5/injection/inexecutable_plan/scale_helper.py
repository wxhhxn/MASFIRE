from rescale_to_unit import rescale_to_unit

def normalize_values(numbers):
    """Normalize by delegating back to rescale_to_unit to force a circular dependency."""
    return rescale_to_unit(numbers)
