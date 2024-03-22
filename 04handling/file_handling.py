'''
FILE HANDLING

text file -> doc, .txt, .html, .py
binary file -> .pdf, .mp3, .mp4, .png, .jpg

for simpler operations and when we do not need any complex structure 

modes:
r -> reads the file (throws an error if file do not exist)
w -> writes in the file (creates an empty file if do not exist)
a -> appends in the file (creates an empty file if do not exist)

file = open(path, mode)
'''
# try:
#     file = open("./exception_handling.py" , "r")
    # print(file)
    # print(file.read())
    # print(file.readlines())
    # print(file.readline())
    # print(file.readline())
    # print(file.readline())
    # print(file.read(5))
    # file.seek(56)
    # print(file.read(5))

#     file.close()
# except IOError as err:
#     print("File do not exist")
#     print(err)

# file = open("./exception_handling.py" , "r")
# data = file.readlines()
# for line in data:
#     print(line)
#     word = line.split()
#     print(word)


# ***********write mode -> It overrides the previous content
# file = open("./copy.txt" , "w")
# file.write("Hey, writing using file handling")
# file.write("Wrting again using file handling")
# file.close()

# *************append mode -> It adds the content at the end of the file
# file = open("./copy.txt", "a")
# # file.write("Hello, writing using the append mode")
# file.writelines(["Hi "," There"] )
# file.close()


# ************with statement
# with open("../02basics/functions.py", "r") as f ,  open("./copy.py" , "w") as f2:
#     for data in f:
#         f2.write(data)
    # print(f.read())


# binary files
# with open("./sst.png", "rb") as f:
#     print(f.read())

# with open("./sst.png" , "rb") as f, open("./copy.png", "wb") as f2:
#     for data in f:
#         f2.write(data)

'''
create a main method which will perform following methods:
create a file
read a file
write in a file
rename a file using os module
deleting a file using os module
'''