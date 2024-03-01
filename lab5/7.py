import re
f=open("row.txt", "r", encoding="UTF8")
def toCamel(snake):
    return snake.group(1).upper()

x = re.sub('_([a-z])', toCamel, f.read())
print(x)