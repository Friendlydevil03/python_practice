class Pycham:
    def Execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    def Execute(self):
        print("Executing")
        print("Compling")
        print("Running")
        print()

class Laptop:
    def Code(self,ide,test):
        ide.Execute()
        test.Execute()

ide1 = Pycham()
ide0 = MyEditor()
lap1 = Laptop()
Laptop().Code(ide1,ide0)
# lap1.Code(ide0,ide1)
lap1.Code(ide1,ide0)