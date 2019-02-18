import math
'''
Check if number is a prime number
'''


def isPrime(number):

    # number = int(input("Enter the number: "))
    if number > 4:
        for i in range(2, math.floor(number**0.5) + 1):
            if number % i == 0:
                return False
            elif i == math.floor(number**0.5):
                return True
    elif number == 2 or number == 3:
        return True
    else:
        return False


# print(isPrime(int(input("Enter the number: "))))
