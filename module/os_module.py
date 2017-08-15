import os

print(os.getcwd())
print(os.chdir(".."))
print(os.getcwd())
print(os.listdir("."))
print(os.access(".",os.F_OK))
