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
        return self.length*self.length #overwritting the area method from super class

aSquare= Square(3)
print(aSquare.area())

#raise RuntimeError('something wrong')