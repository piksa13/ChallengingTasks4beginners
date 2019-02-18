class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 88


class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self) # do you need that? 
        self.length = l

    def area(self):
        return self.length * self.length    # overwriting the area method from super class


try:
    aSquare = Square(int(input('Enter the number: ')))
    print(f'An area method of Square class returns: {aSquare.area()}')
except Exception as err:
    print('Caught an exception')
finally:
    print('     --- End of the script execution. ---     ')

# Raise RuntimeError('something wrong')
