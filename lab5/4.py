import re
f=open("row.txt", "r", encoding="UTF8")
x=re.findall('[A-Z][a-z]+', f.read())
print(x)