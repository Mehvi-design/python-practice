# Function to encode a string using Run-Length Encoding (RLE)
def encodeString(stringVal):
    # Initialize an empty list to store the encoded tuples
    encodelist = []
    
    # Convert the input string into a list of characters for easier manipulation
    stringList = list(stringVal)
    
    # Initialize variables
    i = 0             # Index pointer for traversing the string
    counter = 1       # Counter to count the occurrences of each character
    
    # Loop through the string until the second-last character
    while i < len(stringVal) - 1:
        # If the current character matches the next one, increment the counter
        if stringList[i] == stringList[i + 1]:
            counter += 1
        else:
            # If characters do not match, store the current character and its count
            element = (stringList[i], counter)
            encodelist.append(element)
            
            # Reset the counter for the next character
            counter = 1
        # Move to the next character
        i += 1
    
    # Add the last character (or group of characters) to the list
    encodelist.append((stringVal[i], counter))
    
    # Return the encoded list of tuples
    return encodelist


# Function to decode the Run-Length Encoded list back to the original string
def decodeString(encodedList):
    # Initialize an empty list to store the decoded characters
    decodelist = []
    
    # Loop through each tuple (character, count) in the encoded list
    for char, count in encodedList:
        # Repeat the character `count` times and add to the list
        while count > 0:
            decodelist.append(char)
            count -= 1
    
    # Join the list into a single string and return the decoded string
    decodestring = ''.join(decodelist)
    return decodestring


# Example usage:
# Encoding the input string 'ABBCDEFFFGHIGHg'
Inputstring = encodeString('ABBCDEFFFGHIGHg')
print("Encoded:", Inputstring)

# Decoding the encoded list back to the original string
decodedString = decodeString(Inputstring)
print("Decoded:", decodedString)
