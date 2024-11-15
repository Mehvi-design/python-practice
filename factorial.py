class Answer:
    def factorial(num):
        if type(num)==int and num>=0:
            factorial_num=1
            # Your code goes here.
            for i in range(1,num+1):
                factorial_num=factorial_num*(i)
            return factorial_num
        else:
            return None 

# This is an example of how your code will be called.
# Your function should return the factorial of the number.
# You can edit this code to try different testing cases, which
# will run before the challenge test cases.
number = "spam"
result = Answer.factorial(number)
print(result)