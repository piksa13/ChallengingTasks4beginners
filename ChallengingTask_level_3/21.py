position = [0, 0]
#positiony = 0
n = ''
while True:
    n = input()
    if not n:
        break

    s = n.split(' ')
    if (s[0] == 'DOWN'):
            position[1] -= int(s[1])
    elif (s[0] == 'UP'):
            position[1] += int(s[1])
    elif (s[0] == 'LEFT'):
            position[0] -= int(s[1])
    elif (s[0] == 'RIGHT'):
            position[0] += int(s[1])
    else:
        pass
distance = ((position[0])**2 + (position[1])**2)**(0.5)
print(f'The distance is: {round(distance)}')
#print(position)