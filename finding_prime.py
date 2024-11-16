def allPrimesUpTo(num):
    # Step 1: Generate a list of numbers that are divisible by any number from 2 to num
    # This comprehension generates a list with numbers 'no' from 2 to num,
    # for each 'no', it checks divisibility with every number 'n' from 2 to num.
    numlist = [no for no in range(2, num + 1) for n in range(2, num + 1) if no % n == 0]
    
    # Step 2: Filter out the prime numbers
    # A prime number will only appear once in the numlist because it is only divisible by 1 and itself.
    primelist = [number for number in numlist if numlist.count(number) == 1]
    
    return primelist
def allPrimesUpToSieve_of_Eratosthenes_Algorithm(n):
    # Step 1: Create a list assuming all numbers from 0 to n are prime
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    # Step 2: Use the Sieve of Eratosthenes
    for i in range(2, int(n**0.5) + 1):  # Only go up to the square root of n
        if is_prime[i]:  # If i is still prime
            # Step 3: Mark all multiples of i as non-prime starting from i*i
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    # Step 4: Collect and return all the prime numbers
    return [i for i, prime in enumerate(is_prime) if prime]

# # Example usage
print(allPrimesUpToSieve_of_Eratosthenes_Algorithm(25))  # Output: [2, 3, 5, 7, 11, 13, 17, 19]


# print(allPrimesUpTo(25))


# print(['Monty Python' if n % 6 == 0 else 'Python' if n % 3 == 0 else 'Monty' if n % 2 == 0 else n for n in range(1, 10)])