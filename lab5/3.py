import re
f=open("row.txt", "r", encoding="UTF8")
x=re.findall('[a-z]+_[a-z]+', f.read())
print(x)