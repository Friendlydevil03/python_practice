class A:
    a = 100
    def __init__(self,p):
        self.p = p
    def method1(self):
        print("Parent method")
        print(f"{self.p},a: {self.a}")

class B(A):
    b = 200
    def __init__(self,p,q):
        super().__init__(p)
        self.q = q

    def method2(self):
        print("intermidiate class")
        print(f"{self.q},b:{self.b}")

class C(B):
    c = 300

    def __init__(self, p, q, r):
        super().__init__(p,q)
        self.r = r

    def method3(self):
        print("bottom class")
        print(f"{self.r},c:{self.c}")

class D(C):
    d = 400
    def __init__(self,p,q,r,s):
        super().__init__(p,q,r)
        self.s = s

    def method4(self):
        print("all")
        print(f"{self.s},d:{self.d}")

obj_d = D(11,12,14,15)
obj_d.method4()
obj_d.method3()
obj_d.method2()
obj_d.method1()
print(D.__mro__)
