class QuestionFive():
    def __init__(self):
        #self.s = ''
        print('Write your sentence here:')

    def getString(self):
         self.s = input()

    def stringOut(self):
        print(self.s.upper())

question5 = QuestionFive()
question5.getString()
question5.stringOut()
