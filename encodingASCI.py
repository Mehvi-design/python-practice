# Python code​​​​​​‌‌​​​​‌​​​‌​​​‌‌‌​​‌​​‌​‌ below

def encodeString(stringVal):
    # Your code goes here.
    encodelist=[]
    stringList=list(stringVal)
    i=0
    counter=1
    while i<len(stringVal)-1:
        if(stringList[i]==stringList[i+1]):
            counter=counter+1
        else:
            element=(stringList[i],counter)
            encodelist.append(element)
            counter=1
        i=i+1
    # Add the last character (or group of characters)
    encodelist.append((stringVal[i], counter))
    return encodelist

def decodeString(encodedList):
    # Your code goes here.
    decodelist=[]
    
    for string,key in encodedList:
         while key>0:
           decodelist.append(string)
           key=key-1
    decodestring=''.join(decodelist)
    return decodestring
Inputstring=encodeString('ABBCDEFFFGHIGHg')
print(Inputstring)
print(decodeString(Inputstring))