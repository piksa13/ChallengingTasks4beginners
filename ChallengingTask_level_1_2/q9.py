list2 = ' '
list = []
print('Input one letter')
while True:
    list2 = input()
    if list2 !='q':
        list.append(list2.upper())
        print(list[-1])
        print('Input another letter')
    else:
        print('Goodby')
        break

#sentinel = 'q' # ends when this string is seen
#'\n'.join(iter(input, sentinel))
#for line in iter(input, sentinel):
    #s = input()
    #s = s.upper()# do things here
   # pass





     #list3 =[line.upper() for line in list2]