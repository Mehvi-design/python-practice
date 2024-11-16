# Function to calculate the triangular number of a given integer 'num'
def triangle(num):
    # Base case: if num is 1, the triangular number is simply 1
    if num == 1:
        return num
    # Recursive case: add 'num' to the triangular number of (num - 1)
    return num + triangle(num - 1)

# Function to convert the triangular number to a square-like number
def square(num):
    # Calculate square-like number using two consecutive triangular numbers
    square_num = triangle(num) + triangle(num - 1)
    return square_num

# Function to calculate the factorial of a given number
def factorial(num):
    # If the input is 0, return 1
    if num == 0:
        return 1
    # Calculate factorial using the triangular function recursively
    return num * triangle(num - 1)
inputs=[5,6]
for input in inputs:
    print(f"{input}'s square is: {square(input)}")
