# Function to encode a string using Run-Length Encoding (RLE)
def encodeString(stringVal):
    # Initialize an empty list to store the encoded tuples
    encodelist = []
    counter=0
    prevchar=stringVal[0] #store the previous string value
    for char in stringVal: #go through every character in the string
        if char!=prevchar: #if the character  is same as previous char
            encodelist.append((prevchar,counter))#append the character and the counter in atuple in the list
            counter=0 #reset the counter
        counter +=1#increase the counter
        prevchar=char
    encodelist.append((prevchar,counter))
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
