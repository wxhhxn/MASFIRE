"""
file_name_check.py - Validate resource names according to specific rules

This module provides a function to validate resource names based on multiple conditions:
- Name format requirements
- Digit count constraints
- Extension validation
"""

def file_name_check(file_name):
    """Validate a resource name according to specific rules.

    Args:
        file_name (str): The resource name to validate

    Returns:
        str: 'Yes' if valid, 'No' if invalid

    Rules:
    1. No more than 3 digits in the name
    2. At least 5 characters in the name
    3. Exactly one dot present
    4. Substring before dot is not empty and starts with latin letter
    5. Substring after dot is one of ['txt', 'exe', 'dll']
    """
    # Count digits
    digit_count = sum(c.isdigit() for c in file_name)
    if digit_count > 3:
        return 'No'

    # Check length
    if len(file_name) < 5:
        return 'No'

    # Check dot count and position
    if file_name.count('.') != 1:
        return 'No'

    # Split into name and extension
    parts = file_name.split('.')
    if len(parts) != 2:
        return 'No'

    name_part, ext_part = parts

    # Check name part
    if not name_part:
        return 'No'
    if not name_part[0].isalpha():
        return 'No'

    # Check extension
    valid_extensions = {'txt', 'exe', 'dll'}
    if ext_part not in valid_extensions:
        return 'No'

    return 'Yes'

# Test cases
if __name__ == '__main__':
    test_cases = [
        ("example.txt", "Yes"),
        ("1example.dll", "No"),
        ("file.exe", "No"),  # Too short
        ("longfilename.with.txt", "No"),  # Multiple dots
        ("valid.exe", "No"),  # Too short
        ("validfile.txt", "Yes"),
        ("invalid.dll", "No"),  # Starts with digit
        ("test123.txt", "Yes"),  # Exactly 3 digits
        ("test1234.txt", "No"),  # Too many digits
        ("file.bin", "No"),  # Invalid extension
        (".txt", "No"),  # Empty name part
        ("name.", "No"),  # Empty extension
    ]

    for file_name, expected in test_cases:
        result = file_name_check(file_name)
        print(f"Input: {file_name:<20} Expected: {expected:<5} Got: {result:<5} {'✅' if result == expected else '❌'}")