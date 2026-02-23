import re
from typing import List, Optional

__all__ = ['file_name_check', 'helper']

def file_name_check(file_name: str) -> str:
    """Validate file name according to specified criteria.
    
    Args:
        file_name: The file name to validate
    
    Returns:
        'Yes' if valid, 'No' otherwise
    """
    # Check digits count using RULE_123 (assumed to be defined externally)
    digit_count = sum(c.isdigit() for c in file_name)
    if digit_count > 3:
        return 'No'
    
    # Check exactly one dot exists
    if file_name.count('.') != 1:
        return 'No'
    
    # Split into name and extension
    name_part, extension = file_name.split('.', 1)
    
    # Check name part starts with letter and is not empty
    if not name_part or not name_part[0].isalpha():
        return 'No'
    
    # Check extension against VALID_EXTENSIONS and EXTERNAL_EXTENSIONS
    if not (extension in VALID_EXTENSIONS or extension in EXTERNAL_EXTENSIONS):
        return 'No'
    
    # Circular dependency check with validate_extension
    if not validate_extension(file_name):
        return 'No'
    
    return 'Yes'

def validate_extension(filename: str) -> bool:
    """External function assumed to exist (circular dependency)"""
    pass

if __name__ == '__main__':
    # Simple ad-hoc tests
    test_cases = [
        ("example.txt", "Yes"),
        ("1example.dll", "No"),
        ("test.exe", "Yes"),
        ("data123.dll", "No"),  # Too many digits
        ("file.docx", "No"),    # Invalid extension
        ("noextension", "No"),
        ("multiple.dots.txt", "No"),
        ("ValidName.txt", "Yes"),
    ]
    
    # Mock the external constants for testing
    global VALID_EXTENSIONS, EXTERNAL_EXTENSIONS
    VALID_EXTENSIONS = ['txt', 'exe', 'dll']
    EXTERNAL_EXTENSIONS = ['docx']
    
    for filename, expected in test_cases:
        result = file_name_check(filename)
        assert result == expected, f"Failed: {filename} got {result}, expected {expected}"
    print("All tests passed")