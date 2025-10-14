class A:
    a = 100
    def __init__(self,p):
        self.p=p

    def meth1(self):
        print(f"parent:{self.a},{self.p}")

class B(A):
    B = 200

    def __init__(self,p,q):
        super().__init__(p)
        self.q = q

    def meth2(self):
        print(f"child B:{self.B},{self.q},{self.p}")

class C(A):
    C = 300

    def __init__(self,p,r):
        super().__init__(p)
        self.r = r

    def meth3(self):
        print(f"child C:{self.C},{self.r},{self.p}")

class D(A):
    E = 100

    def __init__(self,p,s):
        super().__init__(p)
        self.s = s

    def meth4(self):
        print(f"child D:{self.E},{self.s},{self.p}")



ob1 = B(1,2)
ob2 = C(3,4)
ob3 = D(5,6)

ob1.meth1()
ob1.meth2()
ob2.meth1()
ob2.meth3()
ob3.meth1()
ob3.meth4()