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

# Test the factorial function with input 2
print(factorial(2))  # Expected output: 2 * triangle(1) = 2 * 1 = 2

# Test the square function with input 5
print(square(5))     # Expected output: triangle(5) + triangle(4) = 15 + 10 = 25
