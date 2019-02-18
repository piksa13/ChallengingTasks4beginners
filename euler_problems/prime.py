import math
'''
Prime numbers generator
'''


def isPrime(number):

    # number = int(input("Enter the number: "))
    if number > 1:
        for i in range(2, math.floor(number**0.5) + 1):
            if number % i == 0:
                return False
            elif i == math.floor(number**0.5):
                return True
    else:
        return False


# print(isPrime(int(input("Enter the number: "))))
