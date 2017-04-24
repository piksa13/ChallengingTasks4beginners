#print(all([0,1,2,3]))
#print(all([1,2,3]))
#mylist = ["hello", "there", "how", "are", "you", ""]
#print(all(mylist))


#a_var = 'I am a global var'

#def a_func():
 #   a_var = 'I am a local var'
  #  print(a_var, '[ a_var inside a_func() ]')

#a_func()
#print(a_var, '[ a_var outside a_func() ]')

a = 'global'

def outer():

    def len(in_var):
        print('called my len() function: ', end="")
        l = 0
        for i in in_var:
            l += 1
        return l

    a = 'local'

    def inner():
        global len
        nonlocal a
        a += ' variable'
    inner()
    print('a is', a)
    print(len(a))

outer()

print(len(a))
print('a is', a)


