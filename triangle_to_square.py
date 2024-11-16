# Python code​​​​​​‌‌​​​​‌​​​‌‌‌​​‌​​‌‌​‌‌​‌ below
def triangle(num):
    if num == 1:
        return num
    return num + triangle(num - 1)

def square(num):
    print(num)


triangle_number=triangle(3)


square(triangle_number)