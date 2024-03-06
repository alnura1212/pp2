import os
x=os.getcwd()
print(x)
if os.path.exists(x):
    print(os.path.basename(x), os.path.dirname(x))