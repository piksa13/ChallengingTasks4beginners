def miniDic(n,m):
    d = dict()
    for i in range(n,m+1):
        d[i]= i**2
    #print(d)
    print(d.keys())
    print(tuple(d.values())) # for (a,b) in d.items: print(b)
    print(d.items()) # returns a list of tuples

miniDic(5,10)