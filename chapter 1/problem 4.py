import os

# specify the directory you want to list
directory = "/" 

# list all files and folders in the directory
try:
    contents = os.listdir(directory)
    print(f"Contents of directory '{directory}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")