import os

dir_list = os.listdir()
print(dir_list)

x = os.getcwd()
path = "../../"
dir_list = os.listdir(path)
print(dir_list)

path = "../"
dir_list = os.listdir(path)
print(dir_list)

print(x)