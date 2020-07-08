# # Coding Quiz: Check for Prime Numbers
# # Prime numbers are whole numbers that have only two factors: 1 and the number itself. The first few prime numbers are 2, 3, 5, 7.

# # For instance, 6 has four factors: 1, 2, 3, 6.
# # 1 X 6 = 6
# # 2 X 3 = 6
# So we know 6 is not a prime number.
# Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

# write your code here
# HINT: You can use the modulo operator to find a factor

primenumber = []
for number in check_prime:
    prime = 0
    for i in range(2, number):

        if number % i == 0:
            print(" {} is NOT a prime number, because {} is a factor of {}".format(
                number, i, number))
            break

        elif i == number-1:
            print(" {} is  a prime number, ".format(number))
