#Scope -> visibility/accessibilty of variables in the program
# local scope
# non-local scope
# global scope
# built-in scope

# global scope
x = 20

def outer():
    # local to the function outer
    # x = 30

    #to change the global variable value
    # global x
    # x = 50
    print("Outer: ", x)

# outer()
# print("Outside: ", x)


def outerFunc():
    x = 30
   
    # print("Outer Function: ", x)

    def innerFunc():
        # local to inner function
        # x = 60
        nonlocal x
        x = 80

        print("Inner Func: ", x)
    innerFunc()
    print("Outer Function: ", x)


outerFunc()
print("Outside: ",x)

'''
Built-in scope: This refers to the scope of built-in functions and 
built-in names such as print(), len(), etc. They are accessible 
from any part of the code.
'''

print(len([1, 2, 3]))