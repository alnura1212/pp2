import re
f=open("row.txt", "r", encoding="UTF8")
x=re.findall('ab{2,3}', f.read())
print(x)