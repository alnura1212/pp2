s=input()
upper=0
lower=0
for x in s:
    if x.isupper():
        upper+=1
    else:
        lower+=1
print(upper, lower)