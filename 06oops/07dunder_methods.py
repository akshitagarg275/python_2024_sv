'''
dunder methods
len() --> __len__

> --> __gt__

+ --> __add__

'''

class Num:
    def __init__(self, n):
        self.num = n

    def __gt__(self, other):
        print(self.num > other.num)

    def __add__(self, other):
        print(self.num + other.num)

    def __str__(self):
        return f"{self.num} is an object of Num class"

obj = Num(5)
# print(obj)

obj2 = Num(3)

# obj + obj2
obj > obj2