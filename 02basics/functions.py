#functions -> to wrap the certain code inside the function so it can be called
# again and again

# Functions are based on DRY principle that it can be reused

'''
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
def function_name(params):
    statements
'''

def func_name(num , num2):
    print(f"num is: {num} and num2 is: {num2}")


# func_name(3,6)
# func_name(23,45)
    
# def calc(num, num2):
#     return num+num2
    
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
# def calc_mul(num, num2):
#     ans = num+num2
#     sub = num - num2
#     return [ans, sub]


def returnDictionary():
    return {"name": "John"}


# print(type(calc_mul(8,4)))
# res, ans = calc_mul(9,4)
# print(f"res is: {res} and ans is: {ans}")

# print(returnDictionary())
print("some lines of code after function calling")



