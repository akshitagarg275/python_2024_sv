'''

def __init__(self)

It acts like a constructor
Constructor : A special method which gets called automatically as soon as the 
              object of the class is created

'''


class Human:

    def __init__(self, name, age):
        self.fullName = name
        self.age = age
        self.eyes = 2
        # print("I am human class object")
    
    def greet(self):
        return f"Welcome, {self.fullName} and age is {self.age}"


obj = Human("sam mathur", 23)
obj1 = Human("John Doe", 24)


print(obj.greet())
print(obj1.greet())