# Multilevel Inheritance

class A:
    def __init__(self) :
        print("I am in class A")
    
    @staticmethod
    def greet():
        print("Hello A")

class B(A):
    def __init__(self):
        super().__init__()
    
    # @staticmethod
    # def greet():
    #     print("Hello B")

class C(B):
    def __init__(self):
        super().__init__()

    # @staticmethod
    # def greet():
    #     print("Hello C")

obj = C()
obj.greet()