a=list(map(int, input().split()))
f=open("9.py", "a")
f=open("9.py", "w")
for x in a:
    z=str(x)
    f.write(z+" ")
f=open("9.py", "r")
print(f.read())
f.close()