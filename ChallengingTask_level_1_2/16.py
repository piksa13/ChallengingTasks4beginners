print('Input numbers separated by comma')
t = [i for i in input().split(',') if int(i) % 2 != 0]
print('Numbers that are not divided by two: ' + ','.join(t))
