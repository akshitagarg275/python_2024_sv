#Loops -> DRY (Donot Repeat Yourself)

# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")

'''
while loop
for loop
'''

#**********while loop
'''
initialization
condition
    statements
increment/decrement
'''

# i = 1

# while i <=5 :
#     print(i)
#     i = i + 1

# *********printing odd nums till 10
# i = 1

# while i<=10:
#     if (i%2 != 0):
#         print(i) 
#     i = i+1


# i = 1
# while i <= 10:
#     print(i)
#     i = i + 2


# *****reverse counting 

# num = 10
# while num >= 0:
#     print(num)
#     num = num - 1

# ****for loop (iterables: strings, list, tuple, dictionary, set)
'''
for element in iterable:
    # for statements
'''

# colors = ["red", "orange", "blue", "yellow", "green"]
# for c in colors:
#     print(c)

# str = "Hey, Hellow, How are you doing?"

# for s in str:
#     print(s, end="")


# *********find the no of digits entered by the user
# num = int(input("Enter a number: "))
# noOfDigits = 0
# while num > 0:
#     noOfDigits = noOfDigits + 1
#     num = num // 10  #re-initializer

# print("no of digits: ", noOfDigits)


# *********adding the digits of the no entered
num = int(input("Enter a number: "))
sum = 0
while num > 0:
    rem = num % 10
    print("rem: ", rem)
    sum = sum + rem
    num = num // 10  #re-initializer
    print("Num re-initialising: ", num)

print("sum of digits: ", sum)