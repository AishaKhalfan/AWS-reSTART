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

# Find and store prime numbers in a file
with open('results.txt', 'w') as file:
    for number in range(1, 251):
        if is_prime(number):
            file.write(str(number) + '\n')

print("Prime numbers between 1 and 250 have been stored in 'results.txt'")
