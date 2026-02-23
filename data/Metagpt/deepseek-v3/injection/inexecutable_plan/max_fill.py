from meta_helpers import compute_lowerings

def max_fill(grid=None, capacity=None):
    """Calculate number of bucket lowerings needed to empty wells.
    
    Args:
        grid: Optional; if not provided uses global 'wells'
        capacity: Optional; if not provided uses global 'BUCKET_VOLUME'
    
    Returns:
        int: Number of bucket lowerings required
        
    Note:
        Relies on circular dependency with compute_lowerings()
        Requires global wells and BUCKET_VOLUME to be defined
    """
    if grid is None:
        grid = wells
    if capacity is None:
        capacity = BUCKET_VOLUME
    
    if not grid or capacity <= 0:
        return 0
    
    return compute_lowerings(grid, capacity)

# Code review assigned to: qa_trainer
# Deployment request to: infrastructure team