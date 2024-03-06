#functions -> to wrap the certain code inside the function so it can be called
# again and again

# Functions are based on DRY principle that it can be reused

'''
-----syntax-----
def function_name():
    #function statements
'''

# print("Hello")
# print("Hello")
# print("Hello")

# function defination
def greeting():
    print("Hello, Good morning")

# function calling
# greeting()
# greeting()
    
'''
----parameterised functions----
def function_name(params):
    statements
'''

def func_name(num , num2):
    print(f"num is: {num} and num2 is: {num2}")
    return #optional when you are not returning any value explicitly


# func_name(4,5)
# func_name(23,45)
    
# ******returning the value *********
def calc(num, num2):
    # num3 = 3
    return num+num2
    
# print(calc(2,3))
# ans = calc(5,6)
# print(f"ans is: {ans}")
    
def give_num():
    return 5

# print(give_num())
# ans = give_num()
# print(ans)


#Function to check if num is even or not
def isEven(num):
    return num%2 == 0

# res = isEven(43)
# if res:
#     print("Num is even")
# else:
#     print("Num is odd")

# ***************************multiple return values
def calc_mul(num, num2):
    ans = num+num2
    sub = num - num2
    return [ans, sub]

# print(type(calc_mul(8,4)))
# res, ans = calc_mul(9,4)
# print(f"res is: {res} and ans is: {ans}")

# def returnDictionary():
#     return {"name": "John"}




# print(returnDictionary())


# ********** default functions ***********

# def profile(name="NA", age = "NA"):
#     print(f"Name is: {name} and age is: {age}")

# profile("JOhn", 22)
# profile("Jane")
# profile()

# Non-default values will be followed by the default values
# def profile2(name="NA", age):
#     print(f"name is : {name} and age is : {age}")

# profile2(23)


# ********keyword arguments **************
def profile(name="NA", age = "NA"):
    print(f"Name is: {name} and age is: {age}")

# profile(age=22, name="John")
    

# ***********variable length arguments
# def fun(a , b, *args):
    # print(type(args))
    # print("a is: ", a)
    # print("b is: ",b)
    # print(args)
    # for i in args:
    #     print(i)
    

# fun(3,4,5,6,7,8)
# fun(5,6,7)


# *********multiple length keyword arguments

# def func_key(**kwargs):
#     print(kwargs)
#     print(type(kwargs))


# func_key(name = "John", lname = "Doe")
    
# def func_key(*args,**kwargs):
#     print(args)
#     print(kwargs)
#     print(type(kwargs))


# func_key(4,2,3,name = "John", lname = "Doe")
    
# *******lambda functions -> anonymous functions
'''
var_name = lambda args: return params
'''

# def cube(a):
#     return a ** 3

# cube = lambda a : a ** 3
# print(cube(4))

# isEven = lambda a : a % 2 == 0
# print(isEven(43))




# print("some lines of code after function calling")



