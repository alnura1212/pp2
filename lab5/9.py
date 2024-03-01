import re
f=open("row.txt", "r", encoding="UTF8")
def spaces(word):
    return ' ' + word.group(0)

p = re.sub(r'[A-Z]', spaces, f.read())
print(p)