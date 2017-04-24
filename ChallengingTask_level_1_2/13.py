digit = 0
d = {'low_letters':0, 'upper_letters':0}
for i in input():
    if i.isdigit():
        digit +=1
    elif i.islower():
        d['low_letters']+=1
    elif i.isupper():
        d['upper_letters']+=1

letters = d['low_letters'] + d['upper_letters']

print('Digits ', digit)
print('Letters ' + str(letters))
print('Upper case ', d['upper_letters'])
print('Lower case ', d['low_letters'])

# d = {'Digits':0, 'Letters':0}
#print('Digits', d('Digits'))