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