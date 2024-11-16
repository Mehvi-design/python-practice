# Python code​​​​​​‌‌​​​​‌​​​‌‌​​‌‌​​​​​​​‌​ below
# Use print("messages...") to debug your solution.
#A prime number is a number that can only be divided by itself and 1 without remainders. 
def allPrimesUpTo(num):
    numlist=[no for no in range(2,num+1) for n in range(2,num+1) if no%n==0]
   
    primelist=[number for number in numlist if numlist.count(number)==1]
    print(primelist)

allPrimesUpTo(40)