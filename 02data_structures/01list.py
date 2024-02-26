#List -> [] or list()
'''
iterables -> that we can loop
mutable -> you can change it
indexing -> each element holds the special position
these allow us to add heterogeneous datatypes
'''

# fruits = ["guava", "papaya", "mango", "grapes", "apple"]
# print("Before: ", fruits)
# print(type(fruits))
# print("length of fruits list: ", len(fruits))
# print("Fruit at first position: ", fruits[0])
# print(fruits[3])


# mutability
# fruits[4] = "pineapple"
# fruits[-1] = "pineapple"
# print("After: ", fruits)


# slicing -> to fetch a part from the list
# list_name[start_ind : end_ind : step]

# fruits = ["guava", "papaya", "mango", "grapes", "apple"]

# print("Slicing data: ", fruits[1 : 4])
# # print("Slicing data: ", fruits[ : : 2])
# print("slicing using neg ind: ",fruits[-4:-1])

# for f in fruits:
#     print(f)

# idx = 0
# length_of_list = len(fruits)
# while idx < length_of_list:
#     print(fruits[idx])
#     idx = idx + 1

# fruits = ["guava", "papaya", "mango", "grapes", "apple", "apple"]
# print("fruits 1: ", fruits)
# fruits.append("orange")
# fruits.extend(["dragon fruit", "orange", "water melon"])
# print("fruits 2: ", fruits)

# print(fruits.count("apple"))


# ****************removing duplicates from the list
fruits = ["guava", "papaya", "mango", "grapes", "apple", "apple"]

# ********pop
# print(fruits.pop(3))
# print("fruits after pop:", fruits )

# while fruits.count("apple"):
#     fruits.remove("apple")
# print(fruits)

# fruits.clear()
# print(fruits)

# *******to know the index of any element
# print("Index of papapya: ", fruits.index("papaya"))
# print("Index of apple: ", fruits.index("apple"))

# Inserting the element at a particular index
# fruits.insert(3, "water melon")
# print(fruits)



# print("sort before: ", fruits)
# fruits.sort()
# print("after sort: ", fruits)

# fruits = ["guava", "papaya", "mango", "grapes", "apple", "apple"]
# print(fruits.reverse())
# print("fruits list after reverse: ", fruits)


# operations

# nums = [1,2,3,4]
nums = list(range(1,5))
# print(nums * 3)
num2 = [5,6,7]

print(nums + num2)

