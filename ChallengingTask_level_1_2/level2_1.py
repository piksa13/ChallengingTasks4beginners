#!/usr/bin/env python
import math
c = 50
h = 30
value = []
items = [x for x in input('Enter numbers separated by comma: ').split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d/h))))))

#value = [str(int(round(math.sqrt(2*c*float(d)/h) for d in items[]]
print(','.join(value))

#or print([str(int((2*C*int(D)/H)**0.5)) for D in input().split(',')])
