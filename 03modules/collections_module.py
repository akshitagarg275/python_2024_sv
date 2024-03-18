from collections import namedtuple, deque, Counter, ChainMap

# Point = namedtuple('Point', ['x', 'y'])
# p = Point(1, 2)
# print(p.x, p.y)

# Student = namedtuple('Student',['name','age','DOB'])
# S = Student("John", 23, 23032000)
# # print(S)

# li = ["Kapil", 45, 22052002]
# print(Student._make(li))

# ***************Deque*******************
# q = deque(['name', 'age', 'dob'])
# print(q)
# print(type(q))

de = deque([3,4,5])

# de.append(8)
# print(de)

# appending from left side
de.appendleft(00)
# print(de)

# de.pop()
# de.popleft()
# print(de)

# *************Counter***********
# lst = ['a','b','a','b','c','b']
# counter = Counter(lst)
# print(counter)

# **************ChainMap*************
     
d1 = {'a': 1, 'b': 2} 
d2 = {'c': 3, 'd': 4} 
d3 = {'e': 5, 'f': 6} 

c = ChainMap(d1, d2, d3)
# print(c)
# print(c.keys())
# print(c.values())

dic3 = { 'g' : 5 } 
c = c.new_child(dic3)
print(c)