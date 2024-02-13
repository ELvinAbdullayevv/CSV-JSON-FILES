# CREATE FOLDER

import sys
import os

if sys.argv[1] == "create" and sys.argv[2] == "folder":
    directory = "NEW Folder"
    parent_directory = "C:/Users/user/Desktop/python/file"
    path = os.path.join(parent_directory, directory)
    os.mkdir(path)  # create a folder
elif sys.argv[1] == "delete" and sys.argv[2] == "folder":
    directory = "New Folder"
    parent_directory = "C:/Users/user/Desktop/python/file"
    path = os.path.join(parent_directory, directory)
    os.rmdir(path) # delete folder

Task2
import sys
inputs=[]
if len(sys.argv)>1:
    a = sys.argv[1]
    if a == "add":
        title1 = input("Enter Series Name: ")
        title2 = input("Enter director name: ")
        title3 = input("Enter series of episodes: ")
        title4 = input("Enter genre: ")
        b = [title1,title2,title3,title4]
        inputs.append(b)
        print(*inputs)


    else:
        print("please write add")

try:
    with open("C:/Users/user/Desktop/python/newtext.txt", "a") as file:
        for item in inputs:
            file.write(str(item) + "\n")
except Exception:
    print("An error occurred while writing to the file:",)
