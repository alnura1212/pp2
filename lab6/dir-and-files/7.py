f=open("1.txt", 'r')
with open("2.txt",'w') as a:
    for line in f.read():
        a.write(line)
z=open("2.txt", 'r')
print(z.read())