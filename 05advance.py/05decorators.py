#Decorators
'''
First Class Objects -> Functions in Python can be used as the arguments
'''

# First Class Functions

# def greet(text):
#     return text.upper()

# print(greet("hello"))

# # passing reference of function in the variable
# yell = greet

# print(yell('good morning'))

# ******Function passed as an argument to another function

# def shout(text):
#     return text.upper()

# def whisper(text):
#     return text.lower()

# def greet(func):
#     greeting = func("I am Learning Python")

#     print(greeting)

# greet(whisper)
# greet(shout)


# *****A Function Returns another function

# def createAdder(x):
#     def adder(y):
#         return x+y
#     return adder

# add_15 = createAdder(15) 
# # print(type(add_15))
# print(add_15(10))



#*********DECORATORS*************
'''
decorators are used to modify the behaviour of a function .
Functions are taken as an argument into another function and
then called inside the wrapper function
'''

#decorator
# def hello_decorator(func):
#     #wrapper function inside it argument function will be called
#     def inner1():
#         print("Hello, inside inner 1, part 1")

#         func()

#         print("Func is executed")
#     return inner1

# # function to be called inside the wrapper
# def function_to_be_called():
#     print("THIS IS THE FUNCTION PASSED ON")


# function_to_be_used = hello_decorator(function_to_be_called)
# function_to_be_used()


# ************ finding the execution time in the decorator
import time
import math

# def calculate_time(func):

#     def inner1(*args, **kwargs):
#         begin = time.time()

#         func(*args , **kwargs)

#         end = time.time()

#         print(f"Total time take to execute {func.__name__} is {end-begin}")
#     return inner1

# @calculate_time
# def factorial(num):

#     time.sleep(2)
#     print(math.factorial(num))

# factorial(5)

# ********** function returns something or an argument is passed
# def hello_decorator(func): #sum_of_two_numbers
#     def inner1(*args, **kwargs):

#         returned_value = func(*args , **kwargs) # 3
#         print("After Execution")

#         return returned_value

#     return inner1

# @hello_decorator
# def sum_of_two_numbers(a,b):
#     print("Inside sum of two numbers function")
#     return a+b

# print(sum_of_two_numbers(1,2))

# ********** Chaining of the decorators

def decor1(func): 
    # sqaure of a num
    def inner(): 
        x = func() 
        return x * x 
    return inner 
 
def decor(func): 
    # multiply by 2
    def inner(): 
        x = func() 
        return 2 * x 
    return inner 


@decor1
@decor
def num():
    return 10

print(num())