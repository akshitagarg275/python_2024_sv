'''
Inheritance

Single Inheritance
Multiple Inheritance
Multilevel Inheritance

'''



# class A:
#     def __init__(self):
#         print("I am class A")


# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("I am class B")

# obj = B()


class Human:

    def __init__(self):
        print("I am Human class")

    
    def breathe(self):
        print("I can breathe")
    
    def eat(self):
        print("I can eat")


class Programmer(Human):

    company = "ABC"

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
p1.eat()