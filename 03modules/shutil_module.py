'''
It offers functions for copying,
moving, and deleting files and directories, as well as archiving operations. 
'''
import shutil

# shutil.copy("./calc.py", "./copy.txt")

# shutil.copytree("../02basics", "../copy_dir")

# renamning file or directory
# shutil.move("../copy_dir", "../copy_folder")


# deleting file or folder
# shutil.rmtree("../copy_folder")

# shutil.make_archive('02basics', 'zip', '../02basics')


# statistics using shutil
usage = shutil.disk_usage('/')
print("Total:", usage.total)
print("Used:", usage.used)
print("Free:", usage.free)

full_path = shutil.which('python')
print("Full path to Python executable:", full_path)
