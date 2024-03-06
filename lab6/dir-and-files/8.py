import os
x=input()
if os.path.exists(x):
    a=x.split("\\")
    b=a.pop()
    os.remove(f"{b}")