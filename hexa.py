# Python code​​​​​​‌‌​​​​‌​​​‌​​​​‌​​​​​‌​‌‌ below
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}


# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    try:
        DecNumber=0
        split_hexNums=list(hexNum)
        i=len(split_hexNums)-1
        for split_hexNum in split_hexNums:
            hexNumber=hexNumbers[split_hexNum]
            power=pow(16,i)
            DecNumber=(hexNumber*power)+DecNumber
            i=i-1
        return DecNumber
    except:
        return None
        

print(hexToDec('CAB'))