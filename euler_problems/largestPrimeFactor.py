'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Result: 6857
'''
import math
import time
from prime import isPrime

number = 600851475143
ceiling = math.floor(number**0.5)
factors_array = []  # Usage: for debugging only
prime_factors_array = []    # Array instead of a single var for largest prime for debugging only
i = 2

start_time = time.time()
while i < ceiling:
    if number % i == 0:
        factors_array.append(i)
        if isPrime(i):
            prime_factors_array.append(i)
    i += 1

elapsed = time.time() - start_time
print(f'{prime_factors_array[-1]} and the time it took to generate is {elapsed}')
