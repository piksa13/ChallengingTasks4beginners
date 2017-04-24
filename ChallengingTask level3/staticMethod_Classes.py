class American(object):
    @staticmethod
    def printNationality():
        '''\nStatic method belongs to the class rather than object of a class.
        A static method invoked without the need for creating an instance of a class.
        It has no access to self.
        '''
        print("America")

anAmerican = American()
anAmerican.printNationality()
American.printNationality()

print(American.printNationality.__doc__)

