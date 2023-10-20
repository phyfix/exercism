# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Initialize an empty list to store prime numbers
prime_numbers = []

# Iterate through numbers from 1 to 1000
for number in range(1, 1001):
    if is_prime(number):
        prime_numbers.append(number)

# Calculate the count of prime numbers
count_of_primes = len(prime_numbers)

print("Prime numbers in the range 1 to 1000:", prime_numbers)
print("Total count of prime numbers:", count_of_primes)



# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Initialize an empty list to store prime numbers
prime_numbers = []

# Initialize the number to 1
number = 1

# Iterate through numbers from 1 to 1000 using a while loop
while number <= 1000:
    if is_prime(number):
        prime_numbers.append(number)
    number += 1

# Calculate the count of prime numbers
count_of_primes = len(prime_numbers)

print("Prime numbers in the range 1 to 1000:", prime_numbers)
print("Total count of prime numbers:", count_of_primes)




# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Initialize an empty list to store prime numbers
prime_numbers = []

# Initialize an empty list to store the index numbers of prime numbers
prime_indices = []

# Iterate through numbers from 1 to 1000
for number in range(1, 1001):
    if is_prime(number):
        prime_numbers.append(number)
        prime_indices.append(number - 1)  # Subtract 1 to get the index (0-based)

# Calculate the count of prime numbers
count_of_primes = len(prime_numbers)

print("Prime numbers in the range 1 to 1000:", prime_numbers)
print("Index numbers of prime numbers:", prime_indices)
print("Total count of prime numbers:", count_of_primes)



