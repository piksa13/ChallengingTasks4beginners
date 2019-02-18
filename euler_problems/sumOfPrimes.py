'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from prime import isPrime
import time


start_time = time.time()
i = 2
total = 0
number = 2000000

while i < number:
    if isPrime(i):
        total += i
    i += 1
elapsed = time.time() - start_time
print(f'{total} was generated in {elapsed:.2f}s')


