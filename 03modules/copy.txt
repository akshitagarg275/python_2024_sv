# To make the calculations -> calculator
import simple , complex


# print(dir())

# res = simple.add(2,3)
# print(res)

# print(complex.add(7))

# print(simple.div(5,2))

# ***************importing specific functions
from simple import add , sub , COMMON_BRANDING
# from complex import add

# print(COMMON_BRANDING)

# print(dir())
# print(add(4,5))
# print(sub(7,4))

# x = 23
# y = 4
# print(add(x,y))


# ***********aliases 
from simple import floorDiv as fd
# print(dir())
# print(fd(5,2))


# print(__name__)



# def main():
#     res = fd(5,2)
#     print("Floor div ans is: ", res)

# if __name__ == "__main__":
#     print("Executing the main function")
#     main()