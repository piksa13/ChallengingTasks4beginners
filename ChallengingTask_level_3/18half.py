n = input().split(',')
print(n)
for i in n:
    #print(i)
    if 6 <= len(i) <= 12:
        #print(i)
        a, b, c = 0, 0, 0
        for j in i:
            #print(j)
            if j.isdigit():
                a += 1
            elif j.islower():
                b += 1
            elif j.isupper():
                c += 1
        #print(a,b,c)
        if a > 0 and b > 0 and c > 0:
            print(i)


