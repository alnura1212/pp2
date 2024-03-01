import re
f=open("row.txt", "r", encoding="UTF8")
def to_snake(camel):
    return '_' + camel.group(0).lower()

x = re.sub(r'[A-Z][a-z]', to_snake, f.read())
print(x)