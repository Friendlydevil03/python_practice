class Exam:
    var = None
    def __init__(self):
        if Exam.var == None:
            Exam.var = self
        else:
            raise Exception("single obj")

obj = Exam()
obj2 = Exam()

