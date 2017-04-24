def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input("Give me the number: "))
print("Here is the list of firts %d finobacci numbers: " %n)
list_fib = [str(fib(x)) for x in range(1, n+1)]
print(','.join(list_fib))

print("Here is enumerate list of fibonnaci numbers: ",[(x,y) for (x,y) in enumerate(list_fib)])

#print(fib(n))
