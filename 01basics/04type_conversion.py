# Type Conversion -> explicitly changing the datatype
'''
int()
boolean()
str()
list() 
tuple()
dict()
set()
'''

# num = str(4)
# print("num is: ", num)
# print("type is: ", type(num))

# age = int("23")
# print("age is: ", age)
# print("type is: ", type(age))


# age = int(23.43)
# print("age is: ", age)
# print("type is: ", type(age))

# # is_valid = int(True)
# is_valid = bool(0)
# print("is_valid: ", is_valid)
# print("type is: ", type(is_valid))


name = list("John Doe")
print("name is :", name)
print("type is: ", type(name))

t_name = tuple(name)
print("tuple name: ", t_name)
print("type of tuple name: ", type(t_name))

s_name = set(name)
print("set name: ", s_name)
print("type of set name: ", type(s_name))