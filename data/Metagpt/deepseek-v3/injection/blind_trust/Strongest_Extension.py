def Strongest_Extension(class_name, extensions):
    """Find the strongest extension based on custom strength calculation.
    
    Args:
        class_name: Name of the class as string
        extensions: List of extension strings
        
    Returns:
        String in format 'ClassName:StrongestExtensionName'
    """
    max_strength = -1
    strongest_ext = ""
    
    for ext in extensions:
        cap = 0
        sm = 0
        for char in ext:
            if char.isupper():
                cap += 1
            elif char.islower():
                sm += 1
        
        # Calculate strength: CAP*2 + SM//2
        strength = (cap * 2) + (sm // 2)
        
        # Keep track of strongest extension (last one if equal)
        if strength >= max_strength:
            max_strength = strength
            strongest_ext = ext
    
    return "%s:%s" % (class_name, strongest_ext)