import os
import shutil

path="D:/Python/Project 102"

print("before copying the files")
print(os.listdir(path))

source="D:/Python/Project 102/image.png"
destination="D:/Python/Project 102/Downloaded"

#copy() copies the desired file to another location
# move() moves the desired file to another location
dest=shutil.move(source, destination)
print("after copying the file")
print("source folder folder:")
print(os.listdir(path))
print("destination folder:")
print(os.listdir(destination))