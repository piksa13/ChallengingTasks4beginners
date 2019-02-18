'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

from prime import isPrime

primes = []
index = 10001
i = 2

while True:
    if isPrime(i):
        primes.append(i)
    if len(primes) == index:
        print(primes[index - 1])
        break
    i += 1


