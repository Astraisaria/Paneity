import os
os.chdir("Temp/")
path = os.getcwd()
f = open("path.txt", "r+")
f.truncate(0)
f.write(path)
f.close()