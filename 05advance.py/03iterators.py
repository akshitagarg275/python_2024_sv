#iterators

'''
iterator -> a method that performs iteration on the iterables (list,tuple, string, dict)
iterable ->  the ones on which iteration is performed
iteration ->  the step by step execution of the element

iterator object implemets two special methods __iter__() and __next__() (iterator protocol)

__iter__() or iter() -> It is called for the initialisation of an iterator. It returns iterator object
__next__() or next() -> This method returns the next value for the iterable

Iterable vs Iteration
The main difference between them is, 
iterable in Python cannot save the state of the iteration,
whereas in iterators the state of the current iteration gets saved.
''' 


# nums = [2,3,4,5,6]

# iterator = iter(nums)
# print(iterator)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# Whenever it reaches the end it gets the stopIteration exception

# for x in iterator:
#     print(x)

# st = "Python"
# iterator = iter(st)
# print(next(iterator))


# enumerate

nums = [2,4,5,6,1]

for idx, val in enumerate(nums):
    print(f"index is {idx} and value is {val}")