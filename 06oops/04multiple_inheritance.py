# Multiple Inheritance

# class A:
#     def __init__(self):
#         print("I am in class A")

# class B:
#     def __init__(self):
#         print("I am in class B")

'''
MRO -> Method Resolution Order
'''

# class C(B,A):
#     def __init__(self):
#         super().__init__()

    
# obj = C()


class Human:

    def __init__(self):
        print("I am Human class")

    
    def breathe(self):
        print("I can breathe")
    
    def eat(self):
        print("I can eat")

class Employee:

    company = "ABC"

    def __init__(self) :
        print("I am inside class employee")
    
    def breathe(self):
        print("I am somhow breathing")
    
    def greet(self):
        print("Welcome  to the company: ", self.company)


class Programmer(Human, Employee):

    

    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
        super().__init__()
        
    def code(self):
        print("I write code")
    
    def breathe(self):
        print("I do hardly have time to breathe")
        super().breathe()


p1 = Programmer("sam", 23, "robotics")
p1.breathe()
# p1.eat()