# strings -> str()
'''
anything written using single ('') or double ("") quotes
triple quotes (""")
iterable, indexing, immutables
'''

# st = "we are learning python"

# print(len(st))

# for s in st:
#     print(s)

# indexing
# print(st[3])

# slicing
# print(st[2: 14])

# st[3] = "ad"

# print(st.capitalize())
# print(st.title())
# print(st.lower())
# print(st.upper())
# print(st.center(50))

# print(st.startswith("We"))
# print(st.endswith('e'))



# st = "we are learning python"
# print(st.find("are"))

# if there is no substring it will return -1
# print(st.find("are", 4))

# print(st.index("are"))
# print(st.index("ae"))

st = "wearelearningpython"
# print(st.isalpha())
# print(st.isalnum())

# st = "   "
# print(st.isspace())

# st ="12124"
# print(st.isdigit())

#TODO: strip
# st = "      wearelearningpython       "
# st = "@@@@@@@@@wearelearningpython"

# print(st.lstrip('#'))
# print(st.rstrip())
# print(st.strip())

#TODO: replace
st = "we are learning python"

# new_str = st.replace('a','@', 1)
# print(new_str)

#TODO: split
# print(st.split(' ' ,2))
# print(st.split('a'))

# email = 'john.doe@google.com'
# print(email.split('@')[1])

# nums = input("Please enter the nums separated by comma").split(',')
# print(nums)

#TODO: join
fname = "John"
lname = "doe"
uname = '.'.join([fname , lname])
# uname = ".".join([fname , lname, '007'])
# uname = "@".join([fname , lname, '007'])

# print(uname)
# domain = "google.com"

# email = '@'.join([uname, domain])
# print(email)


# *************escape sequences
# path = r"C:\new_folder\backup\all"
# print(path)

'''
\" -> "
\' -> '
\\ -> \
\n -> new line
\b -> back space
'''

st = "'python'"
st = '\'hey there\''
# print(st)

# TODO: concatenation
# print("1" + "2")
# print("John " + "Doe")

# print("John " * 3)


# *******formatting the strings
num1 = 5
num2 = 2
ans = num1 + num2  #7
# 5 + 2 = 7
# print(str(num1) + " + " + str(num2) + " = " + str(ans))

# print("{0} + {1} = {2}".format(num1,num2, ans))
# print("{1} + {0} = {2}".format(num1,num2, ans))

# f-strings
# print(f"{num1} + {num2} = {ans}")

# TODO: WAP to know if the given string is pallindrome or not
# madam

word = "madam"
rev_word = word[::-1]
# print(rev_word)

# if word == rev_word:
#     print("It is a pallindrome")
# else:
#     print("It is not a pallindrome")

# TODO: WAP to check if the strings is anagram
# silent
# listen

# w1 = "silent"
# w2 = "listen"

# w1 = "mad"
# w2 = "dam"

# print(sorted(w1))
# print(sorted(w2))

# if sorted(w1) == sorted(w2):
#     print("It is anagram")
# else:
#     print("It is not an anagram")
