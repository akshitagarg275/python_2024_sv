# Exception Handling
'''
Errors: 
    - Syntax error : Not writing the code as per the python rule
    - Logical error : 2 + 2 = 4 , '2' + '2' = 22
    - Runtime error : potentially the error which might occur on code execution

Exception handling: It helps us in handling the potentially occuring errors gracefully
try:
    #try block statements
except:
    # except statements
else:
    It will get executed only if there is no exception
finally:
    print("whether you are having exception it will always get executed")
'''
a = 23
b = 0
# b = 'a'


# ans = a/b
# print(ans)

# try:
#     ans = a/b
#     print("ans is:", ans)
# except ZeroDivisionError as err:
#     print(err)
#     print("Denominator cannot be zero")
# except BaseException as err:
#     print(err)
# else:
#     print("It will get executed if there is no exception")
# finally:
#     print("No matter what I am going to be executed")

# d = {"name" : "John"}
# try:
#     print(d["age"])
# except KeyError as e:
#     print("Key is not present: ",e)
# print("More lines of code")

# *********rasing an exception ***********
# name = "John"
# if name == "John":
#     raise NameError("John is not allowed")


# def func():
#     try:
#         return 4
#     except BaseException as e:
#         return 5
#     return 2

# def func():
#     try:
#         return 4
#     except BaseException as e:
#         return 5
#     else:
#         return 6


def func():
    try:
        return 4
    except BaseException as e:
        return 5
    else:
        return 6
    finally:
        return 7
    

print(func())