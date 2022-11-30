class A():
    def methodA(self):
        print("ini method A")

class B():
    def methodB(self):
        print("ini method B")

class C(A,B):
    pass

lina = C()
lina.methodA()
lina.methodB()