def putNumbers(n):
    i = 0
    #while i<n:
        #j=i
        #i=i+1 # this needs to be before the yield to be executed
    for i in range(n):
        if i%7==0:
            yield i #whatever is underneath won't be executed

#for i in reverse(100):
#print(i)

putnumObj = putNumbers(100) #assigning the generator to the object
for a in putnumObj:
    print(a)