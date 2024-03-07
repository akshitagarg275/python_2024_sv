# dictionary comprehension

key = ['a','b','c','d']
values = [22,33,44,55]

# myDict = {k:v for k,v in zip(key,values)}
# print(myDict)

nums = [3,4,5,6]
myDict2 = {n: n**2 for n in nums }
print(myDict2)