# diamond problem
class A:
    def show(self):
        print("show A")
class B(A):
    def show(self):
        print("show B")
class C(A):
    def show(self):
        print("show C")
class D(C,B):
    pass

objec = D()
objec.show()