# datatypes

# primitive datatypes

# Number
# int -> +ve, -ve , 0

# age = 24
# print("age is :", age)
# print("type of age is :", type(age))

# float -> decimal numbers
# price = 24.53
# print("price is :", price)
# print("type of price is :", type(price))

# complex -> real num +/- imaginary num
#  4 + 5j
# c = 4 + 5j
# print("complex num is :", c)
# print("type of c is: ", type(c))

# Boolean -> True/False
is_valid = True
is_valid = False
print("value in is_valid: ", is_valid)
print("type of is_valid: ", type(is_valid))



# Strings
# anything written within single(''), double(" ") or 
#  triple quotes(''') -> multiline strings

# st = "Python"
# st = 'Python'

# st = 'python' \
#  ' is a PL'

# st = ''' this
# is a multiline
# string
# We 
# are
#             learning python
# '''

# print("string data is: ", st)
# print("type of st is: ", type(st))


# None
# temp = None
# print("temp is : ", temp)
# print("type of temp is: ", type(temp))


# ***************Derived datatypes*****************

# # List -> []
# marks = [12, 46, 57, 54, 56]
# print("Marks are: ", marks)
# print("type of marks: ", type(marks))

# Tuple -> ()
# marks = (12, 46, 57, 54, 56)
# print("Marks are: ", marks)
# print("type of marks: ", type(marks))

# Set -> {}
# marks = {12, 46, 57, 54, 56 }
# print("Marks are: ", marks)
# print("type of marks: ", type(marks))

# dictionary -> {key : value}

student = {
    "name" : "Sam",
    "age" : 23,
    "class": "Python",
    "country" : "India"
}

# print("student details: ", student)
# print("type of student variable: ", type(student))


'''
int()
boolean()
str()
list() 
tuple()
dict()
set()
'''

# range -> range(start, end , step)
# end is not included
# nums = list(range(1 , 11))
# print(nums)
# print("type of nums is: ", type(nums))


eve_nums = tuple(range(0, 11, 2))
print(eve_nums)
print(type(eve_nums))
