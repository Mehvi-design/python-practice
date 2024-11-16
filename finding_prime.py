def allPrimesUpTo(num):
    # Step 1: Generate a list of numbers that are divisible by any number from 2 to num
    # This comprehension generates a list with numbers 'no' from 2 to num,
    # for each 'no', it checks divisibility with every number 'n' from 2 to num.
    numlist = [no for no in range(2, num + 1) for n in range(2, num + 1) if no % n == 0]
    
    # Step 2: Filter out the prime numbers
    # A prime number will only appear once in the numlist because it is only divisible by 1 and itself.
    primelist = [number for number in numlist if numlist.count(number) == 1]
    
    return primelist


allPrimesUpTo(1)