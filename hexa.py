# Dictionary mapping hexadecimal characters ('0'-'F') to their decimal values.
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Function to convert a hexadecimal string to a decimal integer.
# If `hexNum` is not a valid hexadecimal number, it returns `None`.
def hexToDec(hexNum): 
    # First, check if every character in `hexNum` is a valid hexadecimal digit.
    for char in hexNum:
        if char not in hexNumbers:  # If an invalid character is found, return None.
            return None
    
    # Initialize the converted decimal value to 0.
    converted = 0
    
    # Determine the exponent for the leftmost character (i.e., position of the character).
    # The leftmost character has the highest power of 16.
    exponent = len(hexNum) - 1

    # Loop through each character in the hexadecimal string.
    for char in hexNum:
        # Convert the character to its decimal value using the `hexNumbers` dictionary.
        # Multiply by 16 raised to the power of `exponent`.
        converted = converted + (hexNumbers[char] * (16 ** exponent))
        
        # Decrease the exponent by 1 for the next character.
        exponent = exponent - 1
    
    # Return the final converted decimal value.
    return converted

# Example usage: Convert hexadecimal string 'CAB' to its decimal equivalent.
print(hexToDec('CAB'))  # Expected output: 3243
