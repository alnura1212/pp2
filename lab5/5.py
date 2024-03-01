import re
f=open("row.txt", "r", encoding="UTF8")
x=re.findall('a.+b', f.read())
print(x)