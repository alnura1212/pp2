import re
f=open("row.txt", "r", encoding="UTF8")
x=re.sub("\s|,|/.",":", f.read())
print(x)
