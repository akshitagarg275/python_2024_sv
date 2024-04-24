#Generators
'''
Instead of return keyword we use the yield keyword
It returns an iterator that produces a sequence of values when iterated over


def my_gen(arg):
    yield value_to_be_returned
'''

# def nums_func():
#     list1 = list(range(5))
#     return list1
    
# print(nums_func())


# def gen1():
#     yield 1
#     yield 2
#     yield 3


# # for value in gen1():
# #     print(value)

# x = gen1()
# print(x)
# print(next(x))
# print(next(x))
# print(next(x))

# generator for fibonacci series
# 0,1,1,2,3,5,8,11,19,30

def fib(limit):
    a,b = 0,1

    while a < limit:
        yield a
        a, b = b, a+b

#creating an generator object
x = fib(5)
# print(x)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# for i in fib(5):
#     print(i)


# Generator expression 
'''
(expression for item in iterable)
'''

# gen_exp = ( i * 5 for i in range(5) if i%2 ==0)

# print(gen_exp)

# for i in gen_exp:
#     print(i)

# Pipelining the generators
def fibonacci_numbers(nums):
    # print("fib 1:",nums)
    x, y = 0, 1
    for _ in range(nums):
        # print("fib 2:",x)
        yield x
        x, y = y, x+y
        
        

def square(nums):
    print("sq: ",nums)
    for num in nums:
        yield num**2

print(sum(square(fibonacci_numbers(3))))


