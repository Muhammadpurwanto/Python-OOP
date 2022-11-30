# method resolution order
class A:
    def showA(self):
        print("ini adalah show A")
class B:
    def showB(self):
        print("ini adalah show B")
class C(A,B):
    pass
objec = C()
objec.showA()
objec.showB()