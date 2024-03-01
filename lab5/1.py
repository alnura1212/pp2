"""import re
f=open("row.txt", "r", encoding="UTF8")
x=re.findall('ab*', f.read())
print(x)"""

import re

with open("row.txt", "r", encoding="utf-8") as fr:
    reading = fr.readlines()
s = ''.join(reading)

#1 Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
p = re.compile('ab*')
m = p.findall(s)
if m:
    print(m)
else:
    print("ERROR")