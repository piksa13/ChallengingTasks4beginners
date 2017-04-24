li = [1,2,3,4,5,6,7,8,9,10]
squaredNumbers = map(lambda x: x**2, li)
print("Here is lambda variable outcome: ",squaredNumbers)

alter = [x**2 for x in li]
print("Here is compression outcome: ",alter)

evenNumbers = map(lambda x: x**2, filter(lambda x: x%2==0, li))
for i in squaredNumbers:
    print(i)