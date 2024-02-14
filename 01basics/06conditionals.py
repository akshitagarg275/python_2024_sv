# decision statements
'''
only if
if-else pair
nested if else
if---elif ladder
'''
# **********only if
'''
if (condition) :
    if condition statements
'''

# age = int(input("Please enter your age: "))

# if (age >= 18):
#     print("YOu can drive")

# num = 25
# if  (num %2 == 0):
#     print(num , " is even")


# ***********if else pair
# we need if condition for the else part
'''
if (condition) :
    if condition statements
else:
    else statements
'''

# age = int(input("Please enter your age: "))

# if (age >= 18):
#     print("YOu can drive")
# else:
#     print("You cannot drive")

# num = 26
# if  (num %2 == 0):
#     print(num , " is even")
# else:
#     print(num, "is odd")


# ********if -elif ladder
'''
if  (condition):
    if statement
elif (condition):
    elif condition
elif (condition):
    elif condition
else:
    else statement

'''

# num = 0

# if (num > 0):
#     print(num , " is positive")
# elif (num < 0):
#     print(num, " is negative")
# elif (num == 0):
#     print(num, " is zero")

# ************rating system
'''
take rating b/w 1-5
'''

# rating = int(input("Enter the rating: "))

# if rating == 5:
#     print("5 star rating")
# elif rating == 4:
#     print("4 star rating")
# elif rating == 3:
#     print("3 star rating")
# elif rating == 2:
#     print("2 star rating")
# elif rating == 1:
#     print("1 star rating")
# else:
#     print("Please enter the rating b/w 1-5")

# if rating == 5:
#     print("5 star rating")

# if rating == 4:
#     print("4 star rating")

# if rating == 3:
#     print("3 star rating")

# if rating == 2:
#     print("2 star rating")
    
# if rating == 1:
#     print("1 star rating")
# else:
#     print("Please enter the rating b/w 1-5")



# *************grading system

'''
Login into the website
- manual email
- using google
- using facebook
'''

isEmail = False
isGoogle = False
isFacebook = False

# if (isEmail or isFacebook or isGoogle):
#     print("You are signed in ")
# else:
#     print("Use valid method for signin")

# if isEmail:
#     print("Signed in using email")
# elif isGoogle:
#     print("Signed in using google")
# elif isFacebook:
#     print("Signed in using facebook")
# else:
#     print("Use a method to sign in")


# ********Purchasing a prod
isLogin = True
isCart = True
isCard = False

if isLogin:
    if isCart:
        if isCard:
            print("Order placed succcessfully!")
        else:
            print("Enter valid card for payment")
    else:
        print("Cart is empty")
else:
    print("Please Login")


# *********Find greatest among three nums

print("further lines of code")