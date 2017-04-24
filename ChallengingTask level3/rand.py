import random
print(random.randrange(100))
print('Here are random number under 100 with a step of 5:')
print(random.randrange(0, 100,5))

print('\nRandom float:',random.uniform(0,1))

print('\nRandom choice with condition:',random.choice([i for i in range(11) if i%2==0]))
#print(random.choice([i for i in range(11) if (i%5==0 and i%7==0)]))

print('\nHere are five random elements under 100:',random.sample(range(100), 5))

li = [3,6,7,8]
la = list(li)
random.shuffle(li)
print('\nThe random shuffle of',la, 'list is', li,'.')
#print('The random shuffle of list', li,'is', random.shuffle(li))