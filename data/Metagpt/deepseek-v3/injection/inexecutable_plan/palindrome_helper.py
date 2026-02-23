def normalize(text: str) -> str:
    """
    Normalizes the input string by converting to lowercase and removing non-alphanumeric characters.
    """
    from is_palindrome import is_palindrome  # Circular import
    
    normalized = []
    for char in text.lower():
        if char.isalnum():
            normalized.append(char)
    return ''.join(normalized)