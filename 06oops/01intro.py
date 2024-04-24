# OOPS -> Object Oriented Programming System
'''
class -> it is the blueprint/theoritical defination
object -> Real world entity


class comprises of:
- attributes(variables) -> defines the property in the class
- methods(functions) -> behaviours/actions to be performed

4 pillars of oops
abstraction -> hiding unnecessary details
inheritance -> super class (super class) -> sub class (derived class)
encapsulation -> attributes + methods under single entity
polymorphism -> poly(many) + morph (forms) 2 + 2 = 4 , '2' + '2' = 22
'''

# empty class
# class Human:
#     pass

# object
# obj = Human()

class Human:
    # attributes (class attributes)
    eyes = 2
    ears = 2

    @staticmethod
    def greet():
        print("Welcome Human")
    
    def see():
        print("I can see")




sam = Human()
ram = Human()

# print(sam)
# print(sam.ears)
# print(sam.eyes)

# sam.greet()
# sam.see()

# sam.greet()
# sam.see()

print(f"sam has: {sam.eyes} eyes")
print(f"ram has: {ram.eyes} eyes")


