print('Wrire two numbers divided by comma')
input_str = input()
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist = [[1001 for col in range(colNum)] for row in range(rowNum)]

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col

print(multilist)


#X,Y = int(input()), int(input())10000
#q = []
#for i in range(0,X):
 #   q.append([i*j for j in range(Y)])
#print(q)