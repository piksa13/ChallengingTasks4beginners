class Circle(object): #class Circle constructed by a radius
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14

class Rectangle(object): #constructed by a length and width
    def __init__(self, x, y):
        self.wid = x
        self.leng = y
    def area(self):
        return self.wid*self.leng

aCircle = Circle(2)
print(aCircle.area())

aRecObj = Rectangle(2,3)
print(aRecObj.area())

