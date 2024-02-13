# Operations on the data

# unary operator -> It required one operand
# a = -3
# print(a)

# Binary operators -> It requires two operands
# operand operator operand
# Arithmetic Operators:
'''
+ , - , /, *, 
%(modulus) -> It returns the remainder 
// (floor divison) -> It returns the integer quotient
** (exponentation) -> It is for the raise to the power
'''

num1 = 5
num2 = 2

# print("Addition res: ", num1 + num2)
# print("Subtraction res: ", num1 - num2)
# print("Multiplication res: ", num1 * num2)
# print("Divison res: ", num1 / num2)
# print("Floor Divison res: ", num1 // num2)
# print("Remainder res: ", num1 % num2)
# print("Raise to power: ", 5**2)


# Assignment Operator '='
a = 5 + 6
# print(a)

# a = 11 * 2
# a = a * 2
# a*= 2
# print(a)

# *************Conditional -> It returns boolean (True/False)
'''
> : greater than
< : lesser than
>= : greater than equal to (if LHS is either greater or equal to RHS)
<= : lesser than equal to
== : eqaulity
!= : Not equal to
'''

# print(5 < 6)
# print(5 >= 4)
# print(4 >= 4)
# print( 5 == 5)
# print(4 != 6)

# ************Logical Operators
'''

and -> If any one operand in False o/p will be False

or -> If any one i/p is True o/p will be True

not -> It simply reverses the state

'''

# print(5>3 and 4<3)
# print(5>=5 and 4>3 and 4>9)

# falsy values -> False, 0, None, ''

# print(not 0)
# print(not [])
# print(not 'a')


# *********Binary operators
'''
& -> binary and
| -> Binary or
! -> binary not
>> -> right shift
<< -> left shift
^ -> xor
'''

# print(5 & 7)
# print(bin(5))

# print(5 | 7)
# print(bin(7))

# print(5 | 15)
# print(bin(15))


# print(5 ^ 7)


# << left shift (It increase the bits)


# print(4 << 1)
# print(bin(8))

# >> right shift (It decrease the bits)

# print(4 >> 1)

# ****membership (in)

nums = [1,2,3,8,4,5]
# print(1 in nums)
# print(11 not in nums)

# name = 'John'
# print('j' in name)

# *****identity (is) -> It checks the memory address is same or not

a = [1, 2]
print("Id of a:", id(a))

b = [1, 2]
print("Id of b:", id(b))

c = a
print("Id of c: ", id(c))
