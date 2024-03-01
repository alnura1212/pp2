import re
f=open("row.txt", "r", encoding="UTF8")
def splits(words):
    words = re.findall(r'[A-Z][a-z]*', f.read())
    return words

a = ' '.join(splits(f.read)) 
print(a)