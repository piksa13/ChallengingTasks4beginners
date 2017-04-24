s = str(input())
d = {}
li = [i for i in s]

print("Elements of the list:",','.join(['%s' %c for c in li]))

print("Elements of the list:",','.join(li))

for l in li:
    d[l] = d.get( l, 0) + 1
print('\n'.join(['%s, %s' %(a,b) for a,b in sorted(d.items())]))

rev = reversed(li)
print('\nHere is the reversed list:',[i for i in rev])

print('Here an alternative quick solution:',li[::-1])

evenindex = [i for i in li if li.index(i)%2==0]
print('\nEvery second index in the list',evenindex)

print('Here is again quicker solution:',li[::2])

#dic = {}
#s=input()

#for s in s:
#    dic[s] = dic.get(s,0)+1
#print('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))