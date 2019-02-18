'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Result: 232792560
'''
import time


start_time = time.time()
number = 2520

while True:
    for i in range(2, 21):
        if number % i != 0:
            break
    else:
        if i == 20:
            print(number)
            break
    number += 1

elapsed_time = time.time() - start_time
print(f'The script took {elapsed_time}')
