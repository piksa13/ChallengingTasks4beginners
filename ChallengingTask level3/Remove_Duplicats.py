li =[12,24,35,24,88,120,155,88,120,155]
j = 0
while(j < len(li)):
    i = j+1
    while(i< len(li)):
        if (li[i] == li[j]):
            del li[i]
        i += 1
    j+=1
print(li)
