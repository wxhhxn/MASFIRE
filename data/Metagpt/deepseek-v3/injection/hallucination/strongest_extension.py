def Strongest_Extension(class_name, extensions):
    """Find the strongest extension based on character count.
    
    Args:
        class_name: Name of the class as a string
        extensions: List of extension strings to evaluate
        
    Returns:
        String in format 'ClassName.StrongestExtension' where StrongestExtension
        is the extension with highest total character count (uppercase + lowercase).
        In case of ties, the last occurrence in the list is chosen.
    """
    max_strength = -1
    strongest_ext = ""
    
    for ext in extensions:
        upper = sum(1 for c in ext if c.isupper())
        lower = sum(1 for c in ext if c.islower())
        strength = upper + lower
        
        if strength >= max_strength:
            max_strength = strength
            strongest_ext = ext
            
    return f"{class_name}.{strongest_ext}"