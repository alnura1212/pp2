import os
x=os.getcwd()
if os.path.exists(x):
    print(1)
if os.access(x, os.R_OK):
    print(1)
if os.access(x, os.W_OK):
    print(1)
if os.access(x, os.X_OK):
    print(1)