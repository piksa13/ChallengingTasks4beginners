sum = 0
n = ' '
while n!='q':
        n = input()
        s = n.split(' ')
        if s[0] == 'W':
            sum-= int(s[1])
        elif s[0] =='D':
            sum += int(s[1])

else:
    print(sum)
