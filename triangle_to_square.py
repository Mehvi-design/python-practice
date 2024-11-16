# Python code​​​​​​‌‌​​​​‌​​​‌‌‌​​‌​​‌‌​‌‌​‌ below
def triangle(num):
    if num == 1:
        return num
    return num + triangle(num - 1)

def square(num):
    square_num=triangle(num)+triangle(num-1)
    return square_num
#factorial function
def factorial(num):
    if num==0:
        return None
    return num*triangle(num-1)

print(factorial(2))
print(square(5))







