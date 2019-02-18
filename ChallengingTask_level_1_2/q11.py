# s = input().split(',')
outcome = [i for i in input().split(',') if int(i, 2) % 5 == 0]
print('--'.join(outcome))
