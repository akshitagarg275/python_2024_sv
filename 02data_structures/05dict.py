# Dict -> { key : value } , dict ()
# keys -> immutable datatypes int, str, tuple
# mutable , iterable 
# to access any particular value we use the keys

stu = {
    "fname" : "John",
    "lname" : "Doe", 
    "age" : 23,
    "courses" : ["Python", "Jasvascript"],
    "isEnrolled": True,
    "fees" : 234.23
}

# print(stu.items())

# for k,v in stu.items():
#     print(f"key is : {k} and value is: {v}")

# print(stu)
# print(type(stu))

# print("age: " ,stu["age"])
# print(stu["courses"][0])

# print(stu.keys())
# print(stu.values())
# print(stu.items())

# print("BEFORE: ", stu)
# print(stu.pop("age1"))
# print("AFTER: ", stu)

# print(stu.get("fname1", 'NA'))

# print(stu.popitem())

# d = dict(name = "Ram", course = "python")
# print(d)


# d2 = dict(id = 123, **stu)
# d2 = dict(**stu, id = 123)
# print(d2)


# word = "Python Programming"
# keep a count of each char in the string

# freq = {}

# for ch in word:
#     # if key already exists
#     if (freq.get(ch) != None):
#         freq[ch] = freq[ch] + 1

#     else:
#         # first time
#         freq[ch] = 1

# print(freq)

sen = "Hey how are you, we are learning python"
words = sen.split(" ")
# print(words)
freq = {}

for w in words:
    if (freq.get(w) != None):
        freq[w] = freq[w] + 1
    else:
        freq[w] = 1

# print(freq)