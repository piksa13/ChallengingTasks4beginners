li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = filter(lambda x: x%2==0, li)
print(evenNumbers)
for i in evenNumbers:
    print(i)
#outcome = [i for i in li if i%2==0]
#print(outcome)