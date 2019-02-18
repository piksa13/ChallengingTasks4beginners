def createGenerator(a):
    mylist = range(int(a))
    for i in mylist:
        yield i, i*i


income = input('Give me a number: ')
mygenerator = createGenerator(income) # create a generator
print(mygenerator) # mygenerator is an object!<generator object createGenerator at 0xb7555c34>
for i in mygenerator:
    print(f'{i[0]} to second power is {i[1]}')
