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
        prevchar=char#update the prevchar so that it moves forward to stringVal[1] and so on
    encodelist.append((prevchar,counter))#as the counter stops on the last element so this code helps add it
    return encodelist

# Function to decode the Run-Length Encoded list back to the original string
def decodeString(encodedList):
    # Initialize an empty string to store the decoded characters
    decodelist = ''
    
    # Loop through each tuple (character, count) in the encoded list as item
    for item in encodedList:
        #multiply item[0] with item[1] i.e character with count and add it with decodedlist
        decodelist=decodelist+item[0]*item[1] 
    return decodelist 


# Example usage:
# Encoding the input string 'ABBCDEFFFGHIGHg'
Inputstring = encodeString('ABBCDEFFFGHIGHg')
print("Encoded:", Inputstring)

# Decoding the encoded list back to the original string
decodedString = decodeString(Inputstring)
print("Decoded:", decodedString)
